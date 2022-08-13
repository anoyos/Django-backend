import calendar
import time
from django.utils.translation import gettext

from .permissions import TokenPermission
from .utils.api_utils import create_admin_user
from django_filters.rest_framework import DjangoFilterBackend
from requests import delete, request
from rest_framework import generics, status, permissions, views, viewsets
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import render, redirect
from django.utils import translation
from io import BytesIO
from PIL import Image, ImageFile

from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import *
from .serializers import *
from .utils.media_storage import MediaStorage
from api.utils.api_utils import (
    request_body
)

from api.utils.email_utils import (
    sendy_subscribe, sendy_subscribe_v2
)


from django.db.models import Q, Count

from api.utils.ses import (
    send_email, reset_password_email_template, 
    welcome_email_template,
    verification_email_template, contact_email
)

from api.utils.security_utils import TokenGenerator, EmailHandler
import jwt
from django.contrib.auth.hashers import make_password, check_password
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text



def subscribe_newsletter(request):
    if request.method == "POST":

        """
            receive parameter for register user
        """
        data = request_body(request)
        email = data.get("email")
        username = data.get("username")
        sendy_subscribe_v2(email, username)
        return JsonResponse({"code": 200, "msg": "success"})

    else:
        return JsonResponse({"code": 500, "msg": "bad request"})


"""
    Class for all user and auth related fnctions
"""     

class Auth:
    def register(request):
        if request.method == "POST":

            """
             receive parameter for register user
            """
            data = request_body(request)
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            api_host = data.get("api_host")
            origin = data.get("origin")
            verified = data.get("verified")
            social = data.get("social")

            """
             Create jwt to authenticate user (generated used email payload)
            """

            encoded_jwt = jwt.encode({"email": email}, "secret", algorithm="HS256")

            """
             Validation 
             1. email count check
             2. username count check
            """

            username_count = User.objects.filter(username=username).count()
            email_count    = User.objects.filter(email=email).count()

            if username_count:
                return JsonResponse({'err': "Username already exist"})
            if email_count:
    
                """
                Validation 
                1. email exist validation check
                """
                if social:

                    user = list(User.objects.filter(email=email).values('id', 'username', 'token', 'email'))[0]
                    user["msg"] = "Login Successful"
                    return JsonResponse(user)
                return JsonResponse({'err': "Email already exist"})

            """
                Create user using request body and make_password() function 
                creating hash key from the password
            """                
            User.objects.create(
                username=username,
                email=email,
                password=make_password(password),
                first_name=first_name,
                last_name=last_name,
                token=encoded_jwt,
                verified= verified
            )

            try:
                sendy_subscribe(email, username)
            except Exception as e:
                pass

            user = list(User.objects.filter(email=email).values('id', 'username', 'token', 'email', 'first_name', 'last_name'))[0]

            """
                Send verification email after successfull registration
            """     
            username = user["username"]
            email = user["email"]
            account_activation_token = TokenGenerator()
            uid = urlsafe_base64_encode(force_bytes(username))
            verification_token = account_activation_token.make_token(user)
            verification_link = "{}/api/verify-email/{}/{}?origin={}".format(
                api_host, uid, verification_token, origin
            )
            BODY_HTML = verification_email_template(verification_link)
            BODY_HTML = BODY_HTML.replace("linkhere", verification_link)
            
            send_email(
                email, "CGAfrica verification email", BODY_HTML
            )

            return JsonResponse(user)

        elif request.method == "PATCH":
            """
               Partially update first_name and last_name for a specific user using `id` parameter.
            """     

            data = request_body(request)
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            id = data.get("id")
            if (first_name or last_name):
                User.objects.filter(id=id).update(first_name=first_name, last_name=last_name)
            else:
                User.objects.filter(id=id).update(deleted=True)
            return JsonResponse({"msg": "success"})

        elif request.method == "PUT":
            """
               Update user information for a specific user using `id` parameter.
            """     
            data = request_body(request)
            dnd = data.get("dnd")
            mature_content = data.get("mature_content")
            user = data.get("user")
            existing_password = data.get("existing_password")
            new_password = data.get("new_password")
            # existing_username = data.get("existing_username")
            # new_username = data.get("new_username")


            encoded_password = list(User.objects.filter(id=user).values('password'))[0]
            match_password = check_password(existing_password, encoded_password["password"])
            if not match_password:
                return JsonResponse({"err": "Password don't match!"})
            
            User.objects.filter(id=user).update(password=make_password(new_password), mature_content=mature_content, dnd=dnd)
            return JsonResponse({"msg": "success"})

        else:
            """
               Get user information for a specific user using `id` parameter.
            """  

            id = request.GET.get("id")

            if id:
                user = list(User.objects.filter(id=id).values('id', 'username', 'email', 'token', 'verified'))[0]
            else:
                user = list(User.objects.values('id', 'username', 'email'))
            return JsonResponse(user, safe=False)
        


    def verify_email(request, uidb64, token):
        """
            Function to verify email
        """  

        origin = request.GET.get("origin")

        username = force_text(urlsafe_base64_decode(uidb64))
        try:
            user = User.objects.get(username=username)
        except:
            return render(
                request,
                "email-conformation-unsuccess.html",
                context={"message": gettext("Something Went Wrong")},
            )

        account_activation_token = TokenGenerator()
        is_valid_link = account_activation_token.check_token(token=token, user=user)
        if not is_valid_link:
            return render(
                request,
                "email-conformation-unsuccess.html",
                context={
                    "message": gettext("Verification failed. Invalid verification link. Try Again.")
                },
            )

        """
            Mark verified true 
        """  
        user.verified = True
        user.save(update_fields=["verified"])

        BODY_HTML = welcome_email_template()
        BODY_HTML = BODY_HTML.replace("linkhere", origin)
        upload_origin = origin+"/upload"
        BODY_HTML = BODY_HTML.replace("secondlink", upload_origin)

        """
            Send email upon successfll verification
        """  

        send_email(
            user.email, "CGAfrica Welcome email", BODY_HTML
        )

        return render(
            request,
            "email-conformation-success.html",
            context={"message": gettext("Your email is verified.")},
        )


    def login(request):
        """
            Function for login user
        """  

        if request.method == "POST":
            data = request_body(request)
            email = data.get("email")
            password = data.get("password")
            
            """
                User can login using both username and email.
                Below query does that.
            """
            count = User.objects.filter(Q(email=email) | Q(username=email)).count()

            if count:
                encoded_password = list(User.objects.filter(Q(email=email) | Q(username=email)).values('password'))[0]
                match_password = check_password(password, encoded_password["password"])
                if match_password:
                    user = list(User.objects.filter(Q(email=email) | Q(username=email)).values('id', 'username', 'email', 'token', 'first_name', 'last_name', 'role', 'auth_token'))[0]
                    
                    # create auth token
                    admin_user_created = user.get("auth_token")
                    if not admin_user_created:
                        import random
                        temp_add = str(random.randint(10000, 90000000))
                        base_user_id, token = create_admin_user(user["username"], temp_add)
                        BaseUser.objects.filter(id=user["id"]).update(
                            base_user_id=base_user_id,
                            auth_token=token
                        )
                        user["auth_token"] = token
                    return JsonResponse(user)

            return JsonResponse({'err': "Invalid username or password"})


    def forgot_password(request):
        """
            Function for forgot password
        """
        data = request_body(request)
        email = data.get("email")

        try:
            user = User.objects.get(email=email)
        except:
            return JsonResponse({'err': "email doesn't exist"})

        uid = urlsafe_base64_encode(force_bytes(user.username))
        account_activation_token = TokenGenerator()
        verification_token = account_activation_token.make_token(user)

        verification_link = "{}/api/accept-new-password/{}/{}?origin={}".format(
            data.get("api_host"), uid, verification_token, data.get("origin")
        )

        BODY_HTML = reset_password_email_template()
        BODY_HTML = BODY_HTML.replace("usernamehere", user.username)
        BODY_HTML = BODY_HTML.replace("linkhere", verification_link)
        
        send_email(
            email, "CGAfrica Password Reset", BODY_HTML
        )

        return JsonResponse({'msg': "Success"})


    def reset_password(self, request):
        """
            Function for reset password
        """
        data = request_body(request)
        uid = data.get("uid")
        verification_token = data.get("verification_token")
        new_password = data.get("new_password")

        username = force_text(urlsafe_base64_decode(uid))

        user = User.objects.get(username=username)

        account_activation_token = TokenGenerator()
        is_valid_link = account_activation_token.check_token(
            token=verification_token, user=user
        )
        if not is_valid_link:
            return Response(
                {
                    "error": gettext("Either link is expired or invalid."),
                    "status_code": status.HTTP_401_UNAUTHORIZED,
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # TODO: password Validations

        user.password = make_password(new_password)
        user.save(update_fields=["password"])

        return Response(
            {"email": user.email, "message": gettext("Password reset successful")},
            status=status.HTTP_200_OK,
        )
    

    def accept_new_password(request, uid, verification_token):
        if request.method == "POST":
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")
            if new_password != confirm_password:
                return render(
                    request,
                    "email-conformation-unsuccess.html",
                    context={"message": gettext("Password mismatch")},
                )
            username = force_text(urlsafe_base64_decode(uid))
            user = User.objects.get(username=username)
            account_activation_token = TokenGenerator()
            is_valid_link = account_activation_token.check_token(
                token=verification_token, user=user
            )
            if not is_valid_link:
                return render(
                    request,
                    "email-conformation-unsuccess.html",
                    context={"message": gettext("Either link is expired or invalid.")},
                )

            # TODO: password Validations
            user.password = make_password(new_password)
            user.save(update_fields=["password"])
            return redirect("https://www.cgafrica.com/login")
            # return render(
            #     request,
            #     "email-conformation-success.html",
            #     context={"message": gettext("Password reset successful")},
            # )
        else:
            lang_code = translation.get_language()
            return render(
                request,
                "reset_password.html",
                context={"uid": uid, "verification_token": verification_token, "lang_code": lang_code},
            )


"""
This function used to contact us logic
"""
def contact(request):
    if request.method == "POST":
        data = request_body(request)

        subject  = data.get("subject")
        email    = data.get("email")
        message  = data.get("message")
        name     = data.get("name")

        BODY_HTML = contact_email()
        BODY_HTML = BODY_HTML.replace("emailhere", email)
        BODY_HTML = BODY_HTML.replace("messagehere", message)
        BODY_HTML = BODY_HTML.replace("namehere", message)
        
        
        send_email(
            "contact@cgafrica.com", subject, BODY_HTML, "contact@cgafrica.com"
        )
        return JsonResponse({"msg": "success"}, safe=False)
    else:
        return JsonResponse({"msg": "bad request"}, safe=False)



"""
    This class handle media files.
    It store media files to s3 bucket using below class.
"""



ImageFile.LOAD_TRUNCATED_IMAGES = True

class S3MediaView(generics.GenericAPIView):
    queryset = S3MediaFiles.objects.all()
    serializer_class = S3MediaFilesSerializer

    def put(self, request):
        data=request.data
        id = data.get("id")
        image_type = data.get("image_type")
        
        S3MediaFiles.objects.filter(id=id).update(image_type=image_type)
        return Response(
            status=status.HTTP_200_OK,
            data={"msg": "success"},
        )


    def post(self, request):
        data=request.data
        # Add data to s3 Media
        file_type = data.get("file_type")
        user = data.get("user")
        if file_type == "Video":
            video_url = data.get("video_url")
            s3mediarequest = {
                "file_size_unit": "Byte", 
                "video_url": video_url, 
                "cga_file_type": file_type,
                "user": user
            }

            serializer = S3MediaFilesSerializer(data=s3mediarequest)
            serializer.is_valid(raise_exception=True)
            s3_media_data = serializer.save()
        else:
            media_file = data.get("file")

            thumb_size = data.get('file').size/1000
            thumb_size = int(thumb_size)
            i = Image.open(data.get('file'))
            i = i.convert('RGB')
            thumb_io = BytesIO()
            
            """
                It is checking the size of images
                and compressing it.
            """
            if (thumb_size > 2500 and thumb_size < 3000):
                quality = 20
            elif (thumb_size > 2000 and thumb_size < 2500):
                quality = 30
            elif (thumb_size > 1500 and thumb_size < 2000):
                quality = 40
            elif (thumb_size > 1000 and thumb_size < 1500):
                quality = 50
            elif (thumb_size > 500 and thumb_size < 1000):
                quality = 60
            elif (thumb_size > 200 and thumb_size < 500):
                quality = 70
            elif (thumb_size > 50 and thumb_size < 200):
                quality = 80
            elif (thumb_size > 3000 and thumb_size < 5000):
                quality = 10
            elif thumb_size > 5000:
                quality = 5
            else:
                quality = 50

            """
               Saving compressed image to database
            """
            i.save(thumb_io, format='JPEG')
            inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, None, 'thumb.jpeg', 
                                                    'image/jpeg', thumb_io.tell(), None)


            ts = calendar.timegm(time.gmtime())
            folder_name = 'user_artwork_gallery/' + str(user) + "/" + str(ts)
            if media_file:
                media_storage = MediaStorage()
                response = media_storage.store_media_file(user, media_file, inmemory_uploaded_file, file_type, folder_name)
                if response.is_success:
                    s3_media = response.result
                    serializer = S3MediaFilesSerializer(s3_media)
                else:
                    return Response(
                        status=status.HTTP_200_OK,
                        data={"error": gettext("Error while uploading image data")},
                    )

        return Response(
            status=status.HTTP_201_CREATED, data={"s3_media_data": serializer.data}
        )


class UpdateS3MediaView(generics.GenericAPIView):
    queryset = S3MediaFiles.objects.all()
    serializer_class = S3MediaFilesSerializer


    def post(self, request):
        data=request.data
        # Add data to s3 Media
        file_type = data.get("file_type")
        user = data.get("user")
        if file_type == "Video":
            video_url = data.get("video_url")
            s3mediarequest = {
                "file_size_unit": "Byte", 
                "video_url": video_url, 
                "cga_file_type": file_type,
                "user": user
            }

            serializer = S3MediaFilesSerializer(data=s3mediarequest)
            serializer.is_valid(raise_exception=True)
            s3_media_data = serializer.save()
        else:
            media_file = data.get("file")

            thumb_size = data.get('file').size/1000
            thumb_size = int(thumb_size)
            i = Image.open(data.get('file'))
            i = i.convert('RGB')
            thumb_io = BytesIO()
            
            """
                It is checking the size of images
                and compressing it.
            """
            if (thumb_size > 2500 and thumb_size < 3000):
                quality = 20
            elif (thumb_size > 2000 and thumb_size < 2500):
                quality = 30
            elif (thumb_size > 1500 and thumb_size < 2000):
                quality = 40
            elif (thumb_size > 1000 and thumb_size < 1500):
                quality = 50
            elif (thumb_size > 500 and thumb_size < 1000):
                quality = 60
            elif (thumb_size > 200 and thumb_size < 500):
                quality = 70
            elif (thumb_size > 50 and thumb_size < 200):
                quality = 80
            elif (thumb_size > 3000 and thumb_size < 5000):
                quality = 10
            elif thumb_size > 5000:
                quality = 5
            else:
                quality = 50

            """
               Saving compressed image to database
            """
            i.save(thumb_io, format='JPEG', quality=quality)
            inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, None, 'thumb.jpeg', 
                                                    'image/jpeg', thumb_io.tell(), None)


            ts = calendar.timegm(time.gmtime())
            folder_name = 'user_artwork_gallery/' + str(user) + "/" + str(ts)
            if media_file:
                media_storage = MediaStorage()
                response = media_storage.store_media_file(user, media_file, inmemory_uploaded_file, file_type, folder_name)
                if response.is_success:
                    s3_media = response.result
                    serializer = S3MediaFilesSerializer(s3_media)
                else:
                    return Response(
                        status=status.HTTP_200_OK,
                        data={"error": gettext("Error while uploading image data")},
                    )

        return Response(
            status=status.HTTP_201_CREATED, data={"s3_media_data": serializer.data}
        )



class ArtworkMediaView(viewsets.ModelViewSet):
    queryset = ArtworkThumb.objects.all()
    serializer_class = ArtworkMediaSerializer

class TagsView(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['user']


class PostArtworkView(viewsets.ModelViewSet):
    # http_method_names = ["POST"]
    queryset = Artwork.objects.all()
    serializer_class = PostArtworkSerializer


class GetArtworkView(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = GetArtworkSerializer
    http_method_names = ['get']
    permission_classes = [TokenPermission]

    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ["is_winner", "is_mention", 'user', 'is_active', 'is_deleted', 'is_draft', 'is_mature_content', 'is_published', 'artwork_type', 'is_video', "slug", "title", "featured", "is_competition", "competition", "winner", "mention"]
    ordering_fields = ["id", "created_at", "updated_at", "serial", "winner", "mention"]
    search_fields = ['title']

    def get_queryset(self):
        queryset   = Artwork.objects.all()
        id__gt = self.request.query_params.get("id__gt")
        id__lt = self.request.query_params.get("id__lt")

        if id__gt:
            queryset = queryset.filter(id__gt=id__gt)
        if id__lt:
            queryset = queryset.filter(id__lt=id__lt)

        return queryset

class GetArtworkLiteView(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = GetArtworkLiteSerializer
    permission_classes = [TokenPermission]

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['user', 'is_active', 'is_deleted', 'is_draft', 'is_mature_content', 'is_published', 'artwork_type', 'is_video', "slug", "artwork_type", "is_video", "featured", "is_competition"]
    ordering_fields = ["id", "created_at", "updated_at", "serial"]

    def get_queryset(self):
        queryset   = Artwork.objects.all()
        mediums    = self.request.query_params.get("mediums")
        users      = self.request.query_params.get("users")
        categories = self.request.query_params.get("categories")
        id__gt = self.request.query_params.get("id__gt")
        id__lt = self.request.query_params.get("id__lt")
        views = self.request.query_params.get("views")
        
        if mediums:
            queryset = queryset.filter(mediums__in=mediums.split(","))
        if users:
            queryset = queryset.filter(user__in=users.split(","))
        if categories:
            queryset = queryset.filter(categories__in=categories.split(","))
        if views:
            queryset = queryset.annotate(count=Count('views__id')).order_by('-count')


        if id__gt:
            queryset = queryset.filter(id__gt=id__gt)
        if id__lt:
            queryset = queryset.filter(id__lt=id__lt)

        

        return queryset





class CommentLikeView(viewsets.ModelViewSet):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['user', 'comment', 'comment_reply']




class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['user']



class ResumeView(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class SkillsView(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['user']


class ExperiencesView(viewsets.ModelViewSet):
    queryset = Experiences.objects.all()
    serializer_class = ExperiencesSerializer


class AvailabilityView(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer


class SocialView(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer


class UserView(viewsets.ModelViewSet):
    http_method_names = ['get']

    queryset = User.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['username', 'email']
    

class FollowingView(viewsets.ModelViewSet):

    queryset = Following.objects.all()
    serializer_class = FollowingSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['primary_user', 'secondary_user']


class CreateFollowView(viewsets.ModelViewSet):

    queryset = Following.objects.all()
    serializer_class = CreateFollowSerializer



class MediumsView(viewsets.ModelViewSet):

    queryset = Mediums.objects.all()
    serializer_class = MediumsSerializer



class ArticleCommentsView(viewsets.ModelViewSet):
    queryset = ArticleComments.objects.all()
    serializer_class = ArticleCommentsSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['article', 'user']
    
    
class CommentsView(viewsets.ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['artwork', 'user']
    
    




class CommentReplyView(viewsets.ModelViewSet):

    queryset = CommentReply.objects.all()
    serializer_class = CommentReplySerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['user', 'comment']
    

class PostCommentsView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = PostCommentSerializer
    
    def delete(self, id):
        id = self.request.query_params.get("id")
        Comments.objects.filter(id=id).delete()
        return Response({"code": 200})


class PostCommentReplyView(viewsets.ModelViewSet):
    queryset = CommentReply.objects.all()
    serializer_class = PostCommentReplySerializer

    def delete(self, id):
        id = self.request.query_params.get("id")
        CommentReply.objects.filter(id=id).delete()
        return Response({"code": 200})


class LikesView(viewsets.ModelViewSet):

    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['artwork', 'user']



class NotificationView(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['user', 'comment', 'comment_reply', 'like', 'seen']
    ordering_fields = ["id"]


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['title']

class ViewsView(viewsets.ModelViewSet):

    queryset = Views.objects.all()
    serializer_class = ViewsSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['artwork', 'user']


class ArtworkCategoryView(viewsets.ModelViewSet):
    queryset = ArtworkCategory.objects.all()
    serializer_class = ArtworkCategorySerializer


class SoftwaresView(viewsets.ModelViewSet):
    queryset = Softwares.objects.all()
    serializer_class = SoftwaresSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['user', 'software_name']


class CollabratorsView(viewsets.ModelViewSet):

    queryset = Collabrators.objects.all()
    serializer_class = CollabratorsSerializer

    def post(self, request):
        data=request.data

        email            = data.get("email")
        name             = data.get("name")
        is_existing_user = data.get("is_existing_user")
        user             = data.get("user")

        if is_existing_user:
            Collabrators.objects.create(
                email = email,
                name  = name,
                is_existing_user = is_existing_user,
                user_id = user
            )
        else:
            Collabrators.objects.create(
                email = email,
                name  = name,
                is_existing_user = is_existing_user,
            )

            BODY_HTML = reset_password_email_template()
            BODY_HTML = BODY_HTML.replace("usernamehere", user.username)
            
            send_email(
                email, "CGAfrica project", BODY_HTML
            )

        return Response(
            status=status.HTTP_201_CREATED, data={"msg": "success"}
        )


class BlockingView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BlockingSerializer



class CompetitionsView(viewsets.ModelViewSet):
    queryset = Competitions.objects.all()
    serializer_class = CompetitionsSerializer
    http_method_names = ['get']

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['competition_id', 'competition_slug']



"""
    Function handle blocking user
"""
def blocking(request):
    if request.method == "DELETE":
        id = request.GET.get("id")
        Blocking.objects.filter(id=id).delete()
        return JsonResponse({'msg': "success"})
    else:
        user = request.GET.get("user")

        users = list(User.objects.exclude(id=user).values('id', 'username', 'email'))
        blockings = list(Blocking.objects.filter(primary_user=user).values())
        for user in users:
            profile = list(Profile.objects.filter(user_id=user["id"]).values())
            if len(profile):
                user["profile"] = profile[0]

            for blocking in blockings:
                if (user["id"] == blocking["secondary_user_id"]):
                    user["blocked"] = True
                    user["blocking_id"] = blocking["id"]

                
        
        return JsonResponse(users, safe=False)

"""
    Function handle following user
""" 
def following(request):
    if request.method == "DELETE":
        id = request.GET.get("id")
        Following.objects.filter(id=id).delete()
        return JsonResponse({'msg': "success"})
    else:
        user = request.GET.get("user")
        followings = list(Following.objects.filter(primary_user=user).values())
        return JsonResponse(followings, safe=False)


"""
    Function handle followers
""" 

# def followers(request):

#     user = request.GET.get("user")
#     users = list(User.objects.exclude(id=user).values('id', 'username', 'email', 'first_name', 'last_name'))
#     followings = list(Following.objects.filter(secondary_user=user).values())
#     followers = []
#     for user in users:

#         profile = list(Profile.objects.filter(user_id=user["id"]).values())
#         if len(profile):
#             user["profile"] = profile[0]
#         for following in followings:
#             if (user["id"] == following["primary_user_id"]):
#                 followers.append(user)
    
#     return JsonResponse(followers, safe=False)


from settings.settings import STATIC_URL, FRONTEND_URL

def share(request):
    slug = request.GET.get("slug")
    data = list(Artwork.objects.filter(slug=slug).values("media__thumb", "title", "slug"))[0]
    context = {
        "title": data["title"],
        "image": "{}{}".format(STATIC_URL, data["media__thumb"]),
        "redirect_url": "{}/gallery/{}".format(FRONTEND_URL, data["slug"]) 
    }
    return render(request, 'sharing.html', context) 
