from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

from django.shortcuts import render, redirect
from .forms import BookForm
from django.contrib.auth.decorators import login_required

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})

def recent_books(request):
    books = Book.objects.filter(publication_year__gt=2000)
    return render(request, 'bookshelf/recent_books.html', {'books': books})
