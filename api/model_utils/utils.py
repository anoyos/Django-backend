
import os

def get_upload_path(instance, filename):
    return os.path.join(
        'user_profile/{0}/{1}'.format(
         instance.user,
         filename)
    )


def get_upload_article(instance, filename):
    return os.path.join(
        'article/{0}/{1}'.format(
         instance.user,
         filename)
    )


def get_upload_path_banner(instance, filename):
    return os.path.join(
        'profile_banner/{0}/{1}'.format(
         instance.user.id,
         filename)
    )


def get_upload_category(instance, filename):
    return os.path.join(
        'artwork_category/{0}/{1}'.format(
         instance.id,
         filename)
    )

def get_upload_background_image(instance, filename):
    return os.path.join(
        'background_content/{0}/{1}'.format(
         instance.id,
         filename)
    )


def get_upload_logo_image(instance, filename):
    return os.path.join(
        'background_logo/{0}/{1}'.format(
         instance.id,
         filename)
    )


def get_upload_social_image(instance, filename):
    return os.path.join(
        'social_contact/{0}/{1}'.format(
         instance.id,
         filename)
    )

def get_album_upload(instance, filename):
    return os.path.join(
        'album_image/{0}/{1}'.format(
         instance.id,
         filename)
    )

def get_s3_upload_path(instance, filename):
    return os.path.join(
        instance.folder_name,
        filename
    )

def get_software_upload_path(instance, filename):
    return os.path.join(
        'software/{0}/{1}'.format(
         instance.id,
         filename)
    )

def get_artwork_upload_path(instance, filename):
    return os.path.join(
        'artwork_project/{0}/{1}'.format(
         instance.id,
         filename)
    )


def get_resume_upload_path(instance, filename):
    return os.path.join(
        'resume/{0}/{1}'.format(
         instance.id,
         filename)
    )