from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )
        return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
    return Response({"message": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({"message": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)
