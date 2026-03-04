from django.urls import path
from .views import PostViewSet, CommentViewSet, feed, like_post, unlike_post
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls + [
    path('feed/', feed),
    path('posts/<int:pk>/like/', like_post),
    path('posts/<int:pk>/unlike/', unlike_post),
]
