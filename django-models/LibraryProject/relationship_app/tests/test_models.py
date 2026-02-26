
from django.test import TestCase, Client
from django.contrib.auth.models import User
from relationship_app.models import UserProfile

class RoleBasedAccessTests(TestCase):
    def setUp(self):
        # Create users with different roles
        self.admin_user = User.objects.create_user(username="admin", password="pass123")
        UserProfile.objects.filter(user=self.admin_user).update(role="admin")

        self.librarian_user = User.objects.create_user(username="librarian", password="pass123")
        UserProfile.objects.filter(user=self.librarian_user).update(role="librarian")

        self.member_user = User.objects.create_user(username="member", password="pass123")
        UserProfile.objects.filter(user=self.member_user).update(role="member")

        self.client = Client()

    def test_admin_access(self):
        """Admin should access admin_view successfully"""
        self.client.login(username="admin", password="pass123")
        response = self.client.get("/admin-view/")
        self.assertEqual(response.status_code, 200)

    def test_librarian_access_denied_to_admin_view(self):
        """Librarian should be denied access to admin_view"""
        self.client.login(username="librarian", password="pass123")
        response = self.client.get("/admin-view/")
        self.assertEqual(response.status_code, 403)

    def test_member_access_denied_to_admin_view(self):
        """Member should be denied access to admin_view"""
        self.client.login(username="member", password="pass123")
        response = self.client.get("/admin-view/")
        self.assertEqual(response.status_code, 403)

    def test_librarian_access(self):
        """Librarian should access librarian_view successfully"""
        self.client.login(username="librarian", password="pass123")
        response = self.client.get("/librarian-view/")
        self.assertEqual(response.status_code, 200)

    def test_member_access(self):
        """Member should access member_view successfully"""
        self.client.login(username="member", password="pass123")
        response = self.client.get("/member-view/")
        self.assertEqual(response.status_code, 200)

    def test_profile_auto_created(self):
        """UserProfile should auto-create when a new user is registered"""
        new_user = User.objects.create_user(username="newuser", password="pass123")
        self.assertTrue(UserProfile.objects.filter(user=new_user).exists())
