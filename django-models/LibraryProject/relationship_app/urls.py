# relationship_app/urls.py
from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]

