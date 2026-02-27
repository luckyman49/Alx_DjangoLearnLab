from django.db.models.signals import post_migrate, post_save
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.conf import settings

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name == "bookshelf":
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
        viewers_group.permissions.set([view_perm])
        editors_group.permissions.set([edit_perm, create_perm])
        admins_group.permissions.set([view_perm, edit_perm, create_perm, delete_perm])

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def assign_default_group(sender, instance, created, **kwargs):
    if created:
        # Every new user starts as a Viewer by default
        viewers_group = Group.objects.get(name="Viewers")
        instance.groups.add(viewers_group)
