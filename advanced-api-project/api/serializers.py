from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Serializes Book model and validates publication year
class BookSerializer(serializers.ModelSerializer):
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Year cannot be in the future")
        return value

    class Meta:
        model = Book
        fields = '__all__'

# Serializes Author model with nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']