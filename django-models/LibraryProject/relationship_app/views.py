from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"

@user_passes_test(is_admin, login_url='login')
@login_required
def admin_view(request):
    return render(request, "admin_view.html", {"user": request.user})

@user_passes_test(is_librarian, login_url='login')
@login_required
def librarian_view(request):
    return render(request, "librarian_view.html", {"user": request.user})

@user_passes_test(is_member, login_url='login')
@login_required
def member_view(request):
    return render(request, "member_view.html", {"user": request.user})

