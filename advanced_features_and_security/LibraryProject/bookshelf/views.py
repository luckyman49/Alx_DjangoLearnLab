from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book

def index(request):
    return HttpResponse("Hello from the bookshelf app!")

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    # Only users with can_create can access
    return render(request, "bookshelf/book_form.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    # Only users with can_edit can access
    return render(request, "bookshelf/book_form.html")

@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    # Only users with can_delete can access
    return render(request, "bookshelf/book_confirm_delete.html")
