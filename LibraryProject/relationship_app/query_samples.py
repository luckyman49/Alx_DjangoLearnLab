from .models import Book, Library

def books_in_library(library_id):
    return Book.objects.filter(library_id=library_id)

def books_by_author(author_id):
    return Book.objects.filter(author_id=author_id)

def librarian_for_library(library_id):
    library = Library.objects.get(id=library_id)
    return library.librarian
