from django.test import TestCase

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()

class PermissionTests(TestCase):
    def setUp(self):
        # Create users
        self.viewer = User.objects.create_user(username="viewer1", password="test123")
        self.editor = User.objects.create_user(username="editor1", password="test123")
        self.admin = User.objects.create_user(username="admin1", password="test123")

        # Create groups
        viewers_group, _ = Group.objects.get_or_create(name="Viewers")
        editors_group, _ = Group.objects.get_or_create(name="Editors")
        admins_group, _ = Group.objects.get_or_create(name="Admins")

        # Fetch permissions
        view_perm = Permission.objects.get(codename="can_view")
        edit_perm = Permission.objects.get(codename="can_edit")
        create_perm = Permission.objects.get(codename="can_create")
        delete_perm = Permission.objects.get(codename="can_delete")

        # Assign permissions to groups
        viewers_group.permissions.add(view_perm)
        editors_group.permissions.add(edit_perm, create_perm)
        admins_group.permissions.add(view_perm, edit_perm, create_perm, delete_perm)

        # Add users to groups
        self.viewer.groups.add(viewers_group)
        self.editor.groups.add(editors_group)
        self.admin.groups.add(admins_group)

    def test_viewer_permissions(self):
        self.assertTrue(self.viewer.has_perm("bookshelf.can_view"))
        self.assertFalse(self.viewer.has_perm("bookshelf.can_edit"))

    def test_editor_permissions(self):
        self.assertTrue(self.editor.has_perm("bookshelf.can_create"))
        self.assertFalse(self.editor.has_perm("bookshelf.can_delete"))

    def test_admin_permissions(self):
        self.assertTrue(self.admin.has_perm("bookshelf.can_delete"))

