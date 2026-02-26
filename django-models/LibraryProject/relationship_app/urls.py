from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import views as auth_views

from django.urls import path
from .views import add_book, edit_book, delete_book


urlpatterns = [
    path("books/add/", views.add_book, name="add_book/"),
    path("books/<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:book_id>/delete/", views.delete_book, name="delete_book"),
]