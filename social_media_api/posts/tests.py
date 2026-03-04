from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import CustomUser
from .models import Post

class PostsTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='poster', password='pass1234')
        self.client.force_authenticate(user=self.user)
        self.posts_url = '/posts/'
        self.comments_url = '/comments/'

    def test_create_post(self):
        data = {'title': 'My First Post', 'content': 'Hello world!'}
        response = self.client.post(self.posts_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # ✅

    def test_create_comment(self):
        post = Post.objects.create(author=self.user, title='Test Post', content='Content here')
        data = {'post': post.id, 'content': 'Nice post!'}
        response = self.client.post(self.comments_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # ✅
