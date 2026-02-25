from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import views as auth_views

from django.urls import path
from .views import admin_view, librarian_view, member_view


urlpatterns = [
    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view"),
]
