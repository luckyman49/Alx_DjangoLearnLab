from .models import Book, Library, Author, Librarian

def books_in_library(library_id):
    """Return all books in a given library."""
    return Book.objects.filter(author=author)

def books_by_author(author_id):
    """Return all books written by a given author."""
    return Book.objects.filter(author_id=author_id)

def librarian_for_library(library_id):
    """Return the librarian responsible for a given library."""
    library = Library.objects.get(id=library_id)
    return library.librarian

def get_author_by_name(author_name):
    """Return an author object by name."""
    return Author.objects.get(name=author_name)

def get_library_by_name(library_name):
    """Return a library object by name."""
    return Library.objects.get(name=library_name)

def books_in_library_by_name(library_name):
    """Return all books in a library given its name."""
    library = Library.objects.get(name=library_name)
    return library.books.all()

def librarian_by_library(library_id):
    """Return librarian using Librarian.objects.get with library filter."""
    return Librarian.objects.get(library=library_id)
