from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import CustomUser
from posts.models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
class LikesNotificationsTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = CustomUser.objects.create_user(username='user1', password='pass1234')
        self.user2 = CustomUser.objects.create_user(username='user2', password='pass1234')
        self.post = Post.objects.create(author=self.user2, title='Test Post', content='Hello')
        self.client.force_authenticate(user=self.user1)

    def test_like_post_creates_notification(self):
        response = self.client.post(f'/posts/{self.post.id}/like/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Like.objects.filter(user=self.user1, post=self.post).exists())
        self.assertTrue(Notification.objects.filter(recipient=self.user2, actor=self.user1, verb="liked your post").exists())

    def test_unlike_post(self):
        Like.objects.create(user=self.user1, post=self.post)
        response = self.client.post(f'/posts/{self.post.id}/unlike/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Like.objects.filter(user=self.user1, post=self.post).exists())

    def test_get_notifications(self):
        Notification.objects.create(recipient=self.user1, actor=self.user2, verb="followed you", target=self.user2)
        response = self.client.get('/notifications/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
