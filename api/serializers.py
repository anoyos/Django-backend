from re import T
import re
from rest_framework.fields import ReadOnlyField
from .models import *
from rest_framework import serializers
from settings.settings import STATIC_URL





class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = "__all__"





class S3MediaFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = S3MediaFiles
        fields = "__all__"



class MediumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mediums
        fields = "__all__"


class ArtworkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtworkCategory
        fields = "__all__"



class ArtworkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtworkCategory
        fields = "__all__"


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"


class ViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Views
        fields = "__all__"



class SoftwaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Softwares
        fields = "__all__"


class ArtworkMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtworkThumb
        fields = "__all__"
        

class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = "__all__"


class PostArtworkSerializer(serializers.ModelSerializer):
    artist_gallery = serializers.PrimaryKeyRelatedField(queryset=S3MediaFiles.objects.all(), many=True)

    class Meta:
        model = Artwork
        fields = "__all__"

    def create(self, validated_data):
        # get many to may fields 
        artist_gallery = validated_data.pop('artist_gallery')
        collaborator = validated_data.pop('collaborator')
        softwares = validated_data.pop('softwares')
        categories = validated_data.pop('categories')
        mediums = validated_data.pop('mediums')
        tags = validated_data.pop('tags')

        # create artwork 
        artwork = Artwork.objects.create(**validated_data)

        # attach many to may fields 
        artwork.artist_gallery.add(*artist_gallery)
        artwork.collaborator.add(*collaborator)
        artwork.softwares.add(*softwares)
        artwork.categories.add(*categories)
        artwork.mediums.add(*mediums)
        artwork.tags.add(*tags)

        return artwork


class GetArtworkSerializer(serializers.ModelSerializer):
    artist_gallery = S3MediaFilesSerializer(many=True, read_only=True)

    class Meta:
        model = Artwork
        fields = "__all__"
        depth = 1


class GetArtworkLiteSerializer(serializers.ModelSerializer):
    artist_gallery = S3MediaFilesSerializer(many=True, read_only=True)

    class Meta:
        model = Artwork
        fields = "__all__"
        depth = 1
        fields = ("id", "artist_gallery", "title", "description", "updated_at", "media", "is_draft", "slug", "is_competition")


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"


class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = "__all__"

class BasicUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            "id", "username", "first_name", "last_name", "email", "profile",
        )
        depth=1 



class FollowingSerializer(serializers.ModelSerializer):
    primary_user = BasicUserSerializer()
    secondary_user = BasicUserSerializer()

    class Meta:
        model = Following
        fields = ("primary_user", 'id', 'secondary_user', 'updated_at')
        depth=1


class CreateFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = "__all__"



class CommentReplySerializer(serializers.ModelSerializer):
    user = BasicUserSerializer(read_only=True)
    commentlike = CommentLikeSerializer(many=True, read_only=True)
    
    class Meta:
        model = CommentReply
        fields = ("name", "user", 'comment', "id", 'created_at', 'commentlike')
        optional_fields = ['user']
        


class CommentsSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer(read_only=True)
    commentreply = CommentReplySerializer(many=True, read_only=True)
    commentlike = CommentLikeSerializer(many=True, read_only=True)


    class Meta:
        model = Comments
        fields = ("name", "user", 'artwork', "id", 'commentreply', 'created_at', 'commentlike')


class ArticleCommentsSerializer(serializers.ModelSerializer):
    user = BasicUserSerializer(read_only=True)

    class Meta:
        model = ArticleComments
        fields = ("name", "user", 'article', "id", 'created_at', 'updated_at')





class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class PostCommentReplySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommentReply
        fields = ("name", "user", 'comment', "id", 'created_at')
        

class PostCommentSerializer(serializers.ModelSerializer):
    commentreply = CommentReplySerializer(many=True, read_only=True)
    
    class Meta:
        model = Comments
        fields = ("name", "user", 'artwork', "id", 'commentreply', 'created_at')




class ExperiencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experiences
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    resume_skills = SkillsSerializer(many=True, read_only=True)
    experiences = ExperiencesSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = "__all__"


class AvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Availability
        fields = "__all__"


class SocialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Social
        fields = "__all__"

        
class BlockingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blocking
        fields = "__all__"  


class CollabratorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collabrators
        fields = "__all__"  

class NotificationSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    def get_profile(self, obj):
        user = obj.user
        try:
            user = Profile.objects.filter(user_id=user).get()
            image =  user.image
            if image:
                return STATIC_URL + str(image)
            else:
                return ""
        except Exception as e:
            return ""

    class Meta:
        model = Notification
        fields = ("id", "user", "comment", "comment_reply", "like", "created_at", "updated_at", "seen", "profile") 
        depth = 1


class CompetitionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitions
        fields = "__all__" 
        depth = 1


class UsersSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    resume = ResumeSerializer()
    availability = AvailabilitySerializer()
    social = SocialSerializer()

    class Meta:
        model = User
        fields = (
            "id", "username", "first_name", "last_name", "email", "mature_content", "dnd", 
            "created_at", "updated_at", "profile", "resume", "availability", 
            "social"
        )
        depth=1 



        