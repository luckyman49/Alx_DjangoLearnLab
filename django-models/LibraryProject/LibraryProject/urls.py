# LibraryProject/urls.py (project-level)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
    # include auth urls if you want Django's login/logout views
    path('accounts/', include('django.contrib.auth.urls')),
]

