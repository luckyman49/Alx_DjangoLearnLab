from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='blog/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='blog/logout.html'
    ), name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Blog Posts
    path('', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/comment/', views.add_comment, name='add-comment'),

     path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
     path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
     path('posts/new/', views.PostCreateView.as_view(), name='post-create'),


]