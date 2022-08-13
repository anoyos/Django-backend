import boto3
from logging import Logger
from django.conf import settings
from botocore.client import ClientError

from ..serializers import S3MediaFilesSerializer
from botocore.client import Config

s3_signature ={
    'v4':'s3v4',
    'v2':'s3'
}

class MediaStorage:
    class Result:
        def __init__(self, is_success, errors, result=None):
            self.is_success = is_success
            self.errors = errors
            self.result = result

    def store_media_file(self, user, media_file, thumb, file_type, folder_name):
        content_type = media_file.name.split('.')[1]
        content_length = media_file.size

        s3mediarequest = {"file": media_file, "thumb": thumb, "file_size_unit": "Byte",
                          "s3_bucket_name": settings.AWS_STORAGE_BUCKET_NAME, "cga_file_type": file_type,
                          "folder_name": folder_name, "user": user, "user": user,
                          "object_name": str(media_file), "file_size": content_length,
                          "media_type": content_type}

        serializer = S3MediaFilesSerializer(data=s3mediarequest)
        serializer.is_valid(raise_exception=True)
        s3_media = serializer.save()

        return MediaStorage.Result(True, None, s3_media)