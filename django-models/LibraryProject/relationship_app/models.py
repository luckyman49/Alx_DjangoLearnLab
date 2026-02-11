from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Author(models.Model):
    first_name = models.CharField(max_length=100, default="Unknown")
    last_name = models.CharField(max_length=100, default="Unknown")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE,
        related_name="books",
        null=True,
        blank=True
    )
    library = models.ForeignKey(
        "Library",
        on_delete=models.CASCADE,
        related_name="books",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=200, default="Unknown")
    location = models.CharField(max_length=200, default="Unknown")

    def __str__(self):
        return self.name


class Librarian(models.Model):
    first_name = models.CharField(max_length=100, default="Unknown")
    last_name = models.CharField(max_length=100, default="Unknown")
    library = models.OneToOneField(
        "Library",
        on_delete=models.CASCADE,
        related_name="librarian",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
