from operator import mod
from django.db import models
from django_mysql.models import JSONField, Model
from django.utils import timezone
from api.model_utils.utils import (
    get_upload_category, 
    get_album_upload, 
    get_upload_path, 
    get_artwork_upload_path,
    get_upload_path_banner, 
    get_s3_upload_path,
    get_software_upload_path,
    get_resume_upload_path,
    get_upload_article
) 
from api.model_utils.constants import USER_GENDER_CHOICES, FILE_TYPE_CHOICES
from api.utils.api_utils import unique_slugify
from django.contrib.auth.models import User as BaseUser



class FullNameMixin(models.Model):
    name_id    = models.BigAutoField(primary_key = True, unique=False, default=None, blank=True)
    a = models.CharField(max_length=255, default=None, null=True)
    b  = models.CharField(max_length=255, default=None, null=True)


    class Meta:
        abstract = True

    class Meta:
        db_table = 'fullname'


class User(models.Model):
    class Role_Type(models.IntegerChoices):
        REGULAR = 1
        PUBLISHED = 2
        ADMIN = 3
        MODERATOR = 4
    id             = models.BigAutoField(primary_key = True)
    username       = models.CharField(max_length=255, unique=True)
    email          = models.CharField(max_length=255, unique=True)
    token          = models.CharField(max_length=255, unique=True, null=True, blank=True)
    password       = models.CharField(max_length=255)
    role           = models.IntegerField(choices=Role_Type.choices, default=1)
    verified       = models.BooleanField(default=False)
    mature_content = models.BooleanField(default=True)
    dnd            = models.BooleanField(default=False)
    deleted        = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, default=None, null=True)
    last_name  = models.CharField(max_length=255, default=None, null=True)
    created_at     = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at     = models.DateTimeField(auto_now=True, null=True, blank=True)
    base_user      = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name="login", null=True, blank=True)
    auth_token     = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username    

    class Meta:
        db_table = 'cga_user_new'


class Article(models.Model):
    id          = models.BigAutoField(primary_key = True)
    title = models.CharField(max_length=255)
    banner = models.FileField(upload_to=get_upload_article, null=True, blank=True)
    editor_data = models.TextField(default=None, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="article"
    )

    def __str__(self):
        return self.title

class S3MediaFiles(models.Model):
    class IMG_TYPE(models.IntegerChoices):
        ARTWORK = 1
        REFRENCE = 2
        WIP = 3

    id   = models.BigAutoField(primary_key = True)
    file = models.FileField(upload_to=get_s3_upload_path, blank=True, null=True)
    thumb = models.FileField(upload_to=get_s3_upload_path, blank=True, null=True)
    s3_bucket_name = models.CharField(max_length=255, default=None, null=True)
    folder_name = models.CharField(max_length=255, default=None, null=True)
    object_name = models.CharField(max_length=255, default=None, null=True)
    media_type = models.CharField(max_length=255, default=None, null=True)
    file_size = models.BigIntegerField(default=None, null=True)
    image_type = models.IntegerField(choices=IMG_TYPE.choices, default=1)

    file_size_unit = models.CharField(
        max_length=255, default=None, null=True
    )  # description: "Byte,KB,MB,GB"
    file_type = models.CharField(
        max_length=255, default=None, null=True, choices=FILE_TYPE_CHOICES
    )
    video_url = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="users_media_files"
    )
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 's3'

class Profile(models.Model):
    id                  = models.BigAutoField(primary_key = True)
    birthday            = models.DateTimeField(null=True, blank=True)
    country             = models.CharField(max_length=255, null=True, blank=True)
    state               = models.CharField(max_length=255, null=True, blank=True)
    postcode            = models.CharField(max_length=255, null=True, blank=True)
    phone               = models.CharField(max_length=255, null=True, blank=True)
    profession_headline = models.TextField(null=True, blank=True)
    image               = models.FileField(upload_to=get_upload_path, null=True, blank=True)
    profile_banner      = models.FileField(upload_to=get_upload_path_banner, null=True, blank=True)
    user                = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name="profile", unique=True)
    gender              = models.CharField(
                            max_length=255, blank=True, default="", choices=USER_GENDER_CHOICES
                        )
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'profile'

 

class Resume(models.Model):
    id          = models.BigAutoField(primary_key = True)
    about       = models.TextField(null=True, blank=True)
    summary     = models.TextField(null=True, blank=True)
    resume_file = models.FileField(upload_to=get_resume_upload_path, null=True, blank=True)
    user        = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name="resume", unique=True)
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'resume'



class Skills(models.Model):
    id          = models.BigAutoField(primary_key = True)
    title  = models.CharField(max_length=255, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="user_skills")
    resume      = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.CASCADE, related_name="resume_skills")

    class Meta:
        db_table = 'skills'

class Experiences(models.Model):
    id          = models.BigAutoField(primary_key = True)
    company  = models.CharField(max_length=255, null=True, blank=True)
    position  = models.CharField(max_length=255, null=True, blank=True)
    starting_from  = models.IntegerField(null=True, blank=True)
    ending_in  = models.IntegerField(null=True, blank=True)
    country  = models.CharField(max_length=255, null=True, blank=True)
    city  = models.CharField(max_length=255, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="experiences")
    resume      = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.CASCADE, related_name="experiences")

    class Meta:
        db_table = 'experiences'


class Availability(models.Model):
    class Status(models.IntegerChoices):
        full_time       = 0
        contract        = 1
        freelance       = 2
        voulnteer       = 3
        work_experience = 4

    id          = models.BigAutoField(primary_key = True)
    status      = models.IntegerField(choices=Status.choices, default=0)
    other       = models.CharField(max_length=255, null=True, blank=True)
    user        = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name="availability", unique=True)
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'availability'


class Social(models.Model):
    id        = models.BigAutoField(primary_key = True)
    email     = models.CharField(max_length=255, null=True, blank=True)
    phone     = models.CharField(max_length=255, null=True, blank=True)
    website   = models.CharField(max_length=255, null=True, blank=True)
    facebook  = models.CharField(max_length=255, null=True, blank=True)
    twitter   = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    linkedin  = models.CharField(max_length=255, null=True, blank=True)
    youtube   = models.CharField(max_length=255, null=True, blank=True)
    pintrest  = models.CharField(max_length=255, null=True, blank=True)
    vimeo     = models.CharField(max_length=255, null=True, blank=True)
    artstation= models.CharField(max_length=255, null=True, blank=True)

    user      = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name="social")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'social'

class Blocking(models.Model):
    id        = models.BigAutoField(primary_key = True)
    primary_user   = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="primary_blocking")
    secondary_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="secondary_blocking")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'blocking'


class Following(models.Model):
    id        = models.BigAutoField(primary_key = True)
    primary_user   = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="primary_following")
    secondary_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="secondary_following")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'following'


# artwork models

class Softwares(models.Model):
    id        = models.BigAutoField(primary_key = True)
    software_name  = models.CharField(max_length=255)
    software_image = models.FileField(upload_to=get_software_upload_path, blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="softwares")

    # def __str__(self):
    #     return self.software_name

    class Meta:
        db_table = 'software'


class Mediums(models.Model):
    id        = models.BigAutoField(primary_key = True)
    medium_name = models.CharField(max_length=255)
    medium_description    = models.TextField(default=None, null=True)
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    # def __str__(self):
    #     return self.medium_name

    class Meta:
        db_table = 'mediums'

class ArtworkCategory(models.Model):
    id        = models.BigAutoField(primary_key = True)
    category_image = models.FileField(upload_to=get_upload_category, blank=True, null=True)
    category_name           = models.CharField(max_length=255, default=None, null=True)
    category_description    = models.TextField(default=None, null=True)
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="artworkcategory")


    # def __str__(self):
    #     return self.category_name

    class Meta:
        db_table = 'artwork_category'


class Tags(models.Model):
    id          = models.BigAutoField(primary_key = True)
    tag_name    = models.CharField(max_length=255, default=None, null=True)
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="tags")

    class Meta:
        db_table = 'tags'

class Collabrators(models.Model):
    id               = models.BigAutoField(primary_key = True)
    email            = models.CharField(max_length=255, blank=True, null=True)
    is_existing_user = models.BooleanField(default=False)
    user             = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="collabrators")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'collabrators'


class ArtworkThumb(models.Model):
    id                = models.BigAutoField(primary_key = True)
    project_image = models.FileField(upload_to=get_artwork_upload_path, blank=True, null=True)
    thumb         = models.FileField(upload_to=get_artwork_upload_path, blank=True, null=True)

    class Meta:
        db_table = 'media'

class Competitions(models.Model):
    id          = models.BigAutoField(primary_key = True)
    competition_id = models.IntegerField()
    competition_slug = models.CharField(max_length=255)

    def __str__(self):
        return self.competition_slug



class Artwork(models.Model):
    class Type(models.IntegerChoices):
        is_2D = 0
        is_3D = 1
    class Serial(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10
        ELEVEN = 11
        TWELVE = 12
        THIRTEEN = 13
        FOURTEEN = 14
        FIFTEEN = 15
        SIXTEEN = 16
        SEVENTEEN = 17
        EIGHTEEN = 18
        NINGHTEEN = 19
        TWENTY = 20
        TWENTRY_ONE = 21
        TWENTY_TWO = 22
        TWENTY_THREE = 23
        TWENTY_FOUR = 24
        TWENTY_FIVE = 25
        TWENTY_SIX = 26
        TWENTY_SEVEN = 27
        TWENTY_EIGHT = 28
        TWENTY_NINE = 29
        THIRTY = 30
        THIRTY_ONE = 31
        THIRTY_TWO = 32
        THIRTY_THREE = 33
        Hundred = 100

    class Winner(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3

    class Mention(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10

    id                = models.BigAutoField(primary_key = True)
    is_competition    = models.BooleanField(default=False)
    featured          = models.BooleanField(default=False)
    
    serial            = models.IntegerField(choices=Serial.choices, default=100)
    winner            = models.IntegerField(choices=Winner.choices, null=True, blank=True)
    mention           = models.IntegerField(choices=Mention.choices, null=True, blank=True)

    is_winner         = models.BooleanField(default=False)
    is_mention        = models.BooleanField(default=False)

    title             = models.CharField(max_length=255, blank=True, null=True)
    slug              = models.CharField(max_length=255, blank=True, null=True)
    description       = models.TextField(blank=True, null=True)
    is_active         = models.BooleanField(default=True)
    is_draft          = models.BooleanField(default=False)
    is_deleted        = models.BooleanField(default=False)
    is_mature_content = models.BooleanField(default=False)
    is_published      = models.BooleanField(default=True)
    artwork_type      = models.IntegerField(choices=Type.choices, default=0)
    is_video          = models.BooleanField(default=False)
    artist_gallery    = models.ManyToManyField(S3MediaFiles, related_name='artwork', blank=True)
    user              = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="artwork")
    media             = models.OneToOneField(ArtworkThumb, null=True, blank=True, on_delete=models.CASCADE, related_name="artwork")
    collaborator      = models.ManyToManyField(Collabrators, blank=True, related_name="artwork")
    softwares         = models.ManyToManyField(Softwares, blank=True, related_name="artwork")
    categories        = models.ManyToManyField(ArtworkCategory, blank=True, related_name="artwork")
    mediums           = models.ManyToManyField(Mediums, blank=True, related_name="artwork")
    tags              = models.ManyToManyField(Tags, blank=True, related_name="artwork")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)
    competition = models.ForeignKey(Competitions, null=True, blank=True, on_delete=models.CASCADE, related_name="artwork")

    class Meta:
        db_table = 'artwork'

    def save(self, **kwargs):
        slug = "%s" % (self.title) 
        unique_slugify(self, slug) 
        super(Artwork, self).save(**kwargs)

class Likes(models.Model):
    id        = models.BigAutoField(primary_key = True)
    user    = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="likes")
    artwork = models.ForeignKey(Artwork, null=True, blank=True, on_delete=models.CASCADE, related_name="likes")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        db_table = 'likes'


class Views(models.Model):
    id        = models.BigAutoField(primary_key = True)
    user    = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="views")
    artwork = models.ForeignKey(Artwork, null=True, blank=True, on_delete=models.CASCADE, related_name="views")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'views'








class ArticleComments(models.Model):
    id          = models.BigAutoField(primary_key = True)
    name        = models.CharField(max_length=255)
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="articlecomments")
    article     = models.ForeignKey(Article, null=True, blank=True, on_delete=models.CASCADE, related_name="articlecomments")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'articlecomment'


class Comments(models.Model):
    id        = models.BigAutoField(primary_key = True)
    name    = models.CharField(max_length=255)
    user    = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="comments")
    artwork = models.ForeignKey(Artwork, null=True, blank=True, on_delete=models.CASCADE, related_name="comments")
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'comments'


class CommentReply(models.Model):
    id        = models.BigAutoField(primary_key = True)
    name    = models.CharField(max_length=255)
    user    = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="commentreply")
    comment  = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True, related_name='commentreply')
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'comment-reply'



class CommentLike(models.Model):
    id      = models.BigAutoField(primary_key = True)
    user    = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="commentlike")
    comment = models.ForeignKey(Comments, null=True, blank=True, on_delete=models.CASCADE, related_name="commentlike")
    comment_reply = models.ForeignKey(CommentReply, null=True, blank=True, on_delete=models.CASCADE, related_name="commentlike")

    class Meta:
        db_table = 'commentlike'



class Notification(models.Model):
    id         = models.BigAutoField(primary_key = True)    
    user       = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="notification")
    comment    = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True, related_name='notification')
    comment_reply = models.ForeignKey(CommentReply, on_delete=models.CASCADE, null=True, related_name='notification')
    like       = models.ForeignKey(Likes, on_delete=models.CASCADE, null=True, related_name='notification')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    seen       = models.BooleanField(default=False)

    class Meta:
        db_table = 'notification'




