from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("relationship_app.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("add_book/", include("relationship_app.urls")),
    path("edit_book/", include("relationship_app.urls")),
    
]
