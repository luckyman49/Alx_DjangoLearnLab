from django.contrib import admin
from .models import UserProfile

# Register the UserProfile model so it appears in the Django Admin dashboard
admin.site.register(UserProfile)

