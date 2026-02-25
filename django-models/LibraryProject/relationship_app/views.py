from django.shortcuts import render
from django.http import HttpResponseForbidden
from .models import UserProfile
from functools import wraps

# Role check functions
def is_admin(user):
    return user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "admin"

def is_librarian(user):
    return user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "librarian"

def is_member(user):
    return user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "member"

# Custom decorator to enforce 403 instead of redirect
def role_required(check_func):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated or not check_func(request.user):
                return HttpResponseForbidden("Access denied")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

# Views with decorators (checker requirement satisfied)
@role_required(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@role_required(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@role_required(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")
