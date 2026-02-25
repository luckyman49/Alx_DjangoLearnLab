from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

# Role check functions
def is_admin(user):
    if user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "admin":
        return True
    raise PermissionDenied

def is_librarian(user):
    if user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "librarian":
        return True
    raise PermissionDenied

def is_member(user):
    if user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "member":
        return True
    raise PermissionDenied

# Views using @user_passes_test
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")
