import os

from django.db import models
from django.utils import timezone
from ..constants import FILE_TYPE_CHOICES
from .user import User




class S3MediaFiles(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to=get_upload_path, blank=True, null=True)
    thumb = models.FileField(upload_to=get_upload_path, blank=True, null=True)
    s3_bucket_name = models.CharField(max_length=255, default=None, null=True)
    folder_name = models.CharField(max_length=255, default=None, null=True)
    object_name = models.CharField(max_length=255, default=None, null=True)
    media_type = models.CharField(max_length=255, default=None, null=True)
    file_size = models.BigIntegerField(default=None, null=True)
    is_reference_image = models.BooleanField(default=False)
    file_size_unit = models.CharField(
        max_length=255, default=None, null=True
    )  # description: "Byte,KB,MB,GB"
    cga_file_type = models.CharField(
        max_length=255, default=None, null=True, choices=FILE_TYPE_CHOICES
    )
    video_url = models.CharField(max_length=255, default=None, null=True)
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="users_media"
    )


class UserMedia(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="users_media"
    )
    s3 = models.ForeignKey(
        "S3MediaFiles", on_delete=models.CASCADE, related_name="users_media_files"
    )


