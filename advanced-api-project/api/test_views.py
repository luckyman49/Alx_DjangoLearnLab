from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Create an author
        self.author = Author.objects.create(name="George Orwell")

        # Create a book
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

    def test_list_books(self):
        """
        Ensure we can retrieve list of books without authentication.
        """
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        """
        Ensure authenticated user can create a book.
        """
        # Log in the test user
        self.client.login(username='testuser', password='testpass123')

        url = reverse('book-list')
        data = {
            "title": "Animal Farm",
            "publication_year": 1945,
            "author": self.author.id
        }

        response = self.client.post(url, data)
        self.assertEqual(response.data_code, status.HTTP_201_CREATED)