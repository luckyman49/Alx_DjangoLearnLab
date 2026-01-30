from .models import Author, Book, Library

def sample_queries():
    # Query all books by a specific author
    author = Author.objects.get(name="Chinua Achebe")
    books_by_author = Book.objects.filter(author=author)

    # List all books in a library
    library = Library.objects.get(name="Central Library")
    books_in_library = library.books.all()

    # Retrieve the librarian for a library
    librarian = library.librarian

    return {
        "books_by_author": books_by_author,
        "books_in_library": books_in_library,
        "librarian": librarian,
    }
