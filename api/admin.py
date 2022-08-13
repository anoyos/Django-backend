from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class SoftwaresResource(resources.ModelResource):
    class Meta:
        model = Softwares

class SoftwaresAdmin(ImportExportModelAdmin):
    resource_class = SoftwaresResource

class ArtworkCategoryResource(resources.ModelResource):
    class Meta:
        model = ArtworkCategory

class ArtworkCategoryAdmin(ImportExportModelAdmin):
    resource_class = ArtworkCategoryResource


class MediumsResource(resources.ModelResource):
    class Meta:
        model = Mediums

class MediumsAdmin(ImportExportModelAdmin):
    resource_class = MediumsResource


class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource


class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile

class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource

admin.site.register(User, UserAdmin)
admin.site.register(S3MediaFiles)
admin.site.register(ArtworkThumb)
admin.site.register(Resume)
admin.site.register(Availability)
admin.site.register(Social)
admin.site.register(Blocking)
admin.site.register(Following)
admin.site.register(Softwares, SoftwaresAdmin)
admin.site.register(Mediums, MediumsAdmin)
admin.site.register(ArtworkCategory, ArtworkCategoryAdmin)
admin.site.register(Profile, ProfileAdmin)

admin.site.register(Tags)
admin.site.register(Collabrators)
admin.site.register(Artwork)
admin.site.register(Likes)
admin.site.register(Views)
admin.site.register(Comments)
admin.site.register(Skills)
admin.site.register(Experiences)
admin.site.register(Article)
admin.site.register(Competitions)
admin.site.register(ArticleComments)



admin.site.register(CommentLike)

