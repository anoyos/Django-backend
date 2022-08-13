

from api.models import Comments, CommentReply, Likes, Artwork, Notification, User, ArtworkThumb, Profile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from api.utils.ses import comments_email_template, likes_email_template, send_email
from settings.settings import STATIC_URL

@receiver(post_save, sender=Comments) 
def after_comment(sender, instance, **kwargs):
    id = instance.id
    user_id = instance.user_id
    artwork_id = instance.artwork_id

    artwork = Artwork.objects.filter(id=artwork_id).get()
    media_id = artwork.media_id 
    comment_count = Comments.objects.filter(artwork_id=artwork_id).count()
    user = User.objects.filter(id=user_id).get()
    thumb = ArtworkThumb.objects.filter(id=media_id).get()
    profile = Profile.objects.filter(user_id=user_id).get()

    BODY_HTML = comments_email_template()
    BODY_HTML = BODY_HTML.replace("usernamehere", user.username)
    BODY_HTML = BODY_HTML.replace("titlehere", artwork.title)
    BODY_HTML = BODY_HTML.replace("commentcounthere", str(comment_count))
    BODY_HTML = BODY_HTML.replace("frontendoriginhere", "https://www.cgafrica.com")
    BODY_HTML = BODY_HTML.replace("thumbhere", STATIC_URL+ str(thumb.thumb))
    BODY_HTML = BODY_HTML.replace("profilepichere", STATIC_URL+ str(profile.image))

    user = User.objects.filter(id=artwork.user_id).get()
    
    send_email(
        user.email, "CGAfrica artwork comment notification", BODY_HTML
    )


@receiver(post_save, sender=CommentReply) 
def after_comment_reply(sender, instance, **kwargs):
    id = instance.id
    user_id = instance.user_id
    comment_id = instance.comment_id
    comment = Comments.objects.filter(id=comment_id).get()
    artwork_id = comment.artwork_id

    artwork = Artwork.objects.filter(id=artwork_id).get()
    media_id = artwork.media_id 
    comment_count = Comments.objects.filter(artwork_id=artwork_id).count()
    user = User.objects.filter(id=user_id).get()
    thumb = ArtworkThumb.objects.filter(id=media_id).get()
    profile = Profile.objects.filter(user_id=user_id).get()

    BODY_HTML = comments_email_template()
    BODY_HTML = BODY_HTML.replace("usernamehere", user.username)
    BODY_HTML = BODY_HTML.replace("titlehere", artwork.title)
    BODY_HTML = BODY_HTML.replace("commentcounthere", str(comment_count))
    BODY_HTML = BODY_HTML.replace("frontendoriginhere", "https://www.cgafrica.com")
    BODY_HTML = BODY_HTML.replace("thumbhere", STATIC_URL+ str(thumb.thumb))
    BODY_HTML = BODY_HTML.replace("profilepichere", STATIC_URL+ str(profile.image))

    user = User.objects.filter(id=artwork.user_id).get()
    
    send_email(
        user.email, "CGAfrica artwork comment notification", BODY_HTML
    )

@receiver(post_save, sender=Likes) 
def after_like(sender, instance, **kwargs):
    id = instance.id
    user_id = instance.user_id
    artwork_id = instance.artwork_id

    artwork = Artwork.objects.filter(id=artwork_id).get()
    media_id = artwork.media_id 
    like_count = Likes.objects.filter(artwork_id=artwork_id).count()
    user = User.objects.filter(id=user_id).get()
    thumb = ArtworkThumb.objects.filter(id=media_id).get()
    profile = Profile.objects.filter(user_id=user_id).get()

    BODY_HTML = likes_email_template()
    BODY_HTML = BODY_HTML.replace("usernamehere", user.username)
    BODY_HTML = BODY_HTML.replace("titlehere", artwork.title)
    BODY_HTML = BODY_HTML.replace("likecounthere", str(like_count))
    BODY_HTML = BODY_HTML.replace("frontendoriginhere", "https://www.cgafrica.com")
    BODY_HTML = BODY_HTML.replace("thumbhere", STATIC_URL+ str(thumb.thumb))
    BODY_HTML = BODY_HTML.replace("profilepichere", STATIC_URL+ str(profile.image))

    user = User.objects.filter(id=artwork.user_id).get()

    send_email(
        user.email, "CGAfrica artwork like notification", BODY_HTML
    )




@receiver(pre_save, sender=Artwork) 
def after_comment(sender, instance, **kwargs):
    serial = instance.serial

    count = Artwork.objects.filter(serial=serial).count()
    if count:
        Artwork.objects.filter(serial=serial).update(
            serial=100
        )
    

@receiver(post_save, sender=Artwork) 
def after_comment(sender, instance, **kwargs):

    artwork  = Artwork.objects.filter(id=instance.id).get()
    
    if artwork.winner:
        Artwork.objects.filter(id=instance.id).update(is_winner=True)
    if artwork.mention:
        Artwork.objects.filter(id=instance.id).update(is_mention=True)




@receiver(post_save, sender=CommentReply) 
def create_notification(sender, instance, **kwargs):
    id         = instance.id
    comment_id = instance.comment_id

    comment = Comments.objects.filter(id=comment_id).get()
    artwork    = Artwork.objects.filter(id=comment.artwork_id).get()
    user       = artwork.user_id

    Notification.objects.create(
        comment_reply_id=id,
        user_id=user
    )



@receiver(post_save, sender=Comments) 
def create_notification(sender, instance, **kwargs):
    id = instance.id
    artwork = instance.artwork_id
    artwork = Artwork.objects.filter(id=artwork).get()
    user    = artwork.user_id

    Notification.objects.create(
        comment_id=id,
        user_id=user
    )


@receiver(post_save, sender=Likes) 
def create_notification(sender, instance, **kwargs):
    id      = instance.id

    artwork = instance.artwork_id
    artwork = Artwork.objects.filter(id=artwork).get()
    user    = artwork.user_id

    Notification.objects.create(
        like_id=id,
        user_id=user
    )