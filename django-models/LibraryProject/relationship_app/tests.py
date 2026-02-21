from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class RBACSmokeTests(TestCase):
    def test_userprofile_created(self):
        u = User.objects.create_user(username='tuser', password='pass')
        self.assertTrue(hasattr(u, 'userprofile'))
