from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import CustomUser
from posts.models import Post

class AccountsTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/register/'
        self.login_url = '/login/'
        self.profile_url = '/profile/'

    def test_user_registration(self):
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'pass1234'}
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # ✅

    def test_user_login(self):
        CustomUser.objects.create_user(username='testuser', email='test@example.com', password='pass1234')
        data = {'username': 'testuser', 'password': 'pass1234'}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # ✅

    def test_profile_access(self):
        user = CustomUser.objects.create_user(username='testuser', password='pass1234')
        self.client.force_authenticate(user=user)
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # ✅


class FollowFeedTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = CustomUser.objects.create_user(username='user1', password='pass1234')
        self.user2 = CustomUser.objects.create_user(username='user2', password='pass1234')
        self.client.force_authenticate(user=self.user1)

    def test_follow_user(self):
        response = self.client.post(f'/follow/{self.user2.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # ✅

    def test_feed(self):
        post = Post.objects.create(author=self.user2, title='Feed Post', content='From user2')
        self.user1.following.add(self.user2)
        response = self.client.get('/feed/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # ✅
