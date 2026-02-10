from .models import Book, Library

def books_in_library(library_id):
    """Return all books in a given library."""
    return Book.objects.filter(library_id=library_id)

def books_by_author(author_id):
    """Return all books written by a given author."""
    return Book.objects.filter(author_id=author_id)

def librarian_for_library(library_id):
    """Return the librarian responsible for a given library."""
    library = Library.objects.get(id=library_id)
    return library.librarian
def Library.objects.get(name=library_name)", "books.all()