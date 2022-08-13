
from django.urls import path, include
from .views import (
    S3MediaView, 
    UpdateS3MediaView,
    PostArtworkView, 
    GetArtworkView,
    ArtworkMediaView, 
    Auth, 
    ProfileView,
    ResumeView,
    SkillsView,
    ExperiencesView,
    AvailabilityView,
    SocialView,
    UserView,
    BlockingView,
    blocking,
    following,
    FollowingView,
    CollabratorsView,
    MediumsView,
    ArtworkCategoryView,
    SoftwaresView,
    GetArtworkLiteView,
    TagsView,
    CommentsView,
    PostCommentsView,
    LikesView,
    ViewsView,
    contact,
    CommentReplyView,
    PostCommentReplyView,
    CreateFollowView,
    share,
    ArticleView,
    NotificationView,
    subscribe_newsletter,
    CompetitionsView,
    CommentLikeView,
    ArticleCommentsView
)
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

router = routers.DefaultRouter()
router.register("notification", NotificationView)
router.register("comment", CommentsView)
router.register("comment-reply", CommentReplyView)
router.register("post-comment", PostCommentsView)
router.register("post-comment-reply", PostCommentReplyView)
router.register("like", LikesView)
router.register("view", ViewsView)
router.register("post-artwork", PostArtworkView)
router.register("tag", TagsView)
router.register("get-artwork", GetArtworkView)
router.register("get-artwork-lite", GetArtworkLiteView)
router.register("artwork-media", ArtworkMediaView)
router.register("user-profile", ProfileView)
router.register("resume", ResumeView)
router.register("skills", SkillsView)
router.register("experiences", ExperiencesView)
router.register("availability", AvailabilityView)
router.register("social", SocialView)
router.register("user", UserView)
router.register("block", BlockingView)
router.register("collabrator", CollabratorsView)
router.register("follow", FollowingView)
router.register("create-follow", CreateFollowView)
router.register("medium", MediumsView)
router.register("categories", ArtworkCategoryView)
router.register("softwares", SoftwaresView)
router.register("article", ArticleView)
router.register("competition", CompetitionsView)
router.register("comment-like", CommentLikeView)
router.register("article-comment", ArticleCommentsView)



urlpatterns = [
    path('s3-media/', S3MediaView.as_view()),
    path('update-s3-media/', UpdateS3MediaView.as_view()),
    # auth related apis
    path('login/', Auth.login),
    path('register/', Auth.register),
    path('forgot-password/', Auth.forgot_password),

    # django html views
    path(
        "accept-new-password/<str:uid>/<str:verification_token>",
        csrf_exempt(Auth.accept_new_password),
        name="accept_new_password",
    ),
    path(
        "reset-password",
        csrf_exempt(Auth.reset_password),
        name="reset_password",
    ),
    path(
        "verify-email/<str:uidb64>/<str:token>",
        csrf_exempt(Auth.verify_email),
        name="user_verify_email",
    ),

    # blocking apis
    path('blocking/', blocking),
    # following apis
    path('following/', following),
    # path('followers/', followers),

    # contact api route 
    path('contact/', contact),
    path('share/', share),
    path('subscribe_newsletter/', subscribe_newsletter),


    path('', include(router.urls)),

]
