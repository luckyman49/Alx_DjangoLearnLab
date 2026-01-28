from django import forms
from .models import Book
from datetime import date

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    # Prevent duplicate book titles
    def clean_title(self):
        title = self.cleaned_data['title']
        if Book.objects.filter(title=title).exists():
            raise forms.ValidationError("This book title already exists.")
        return title

    # Ensure publication year is not in the future
    def clean_publication_year(self):
        year = self.cleaned_data['publication_year']
        current_year = date.today().year
        if year > current_year:
            raise forms.ValidationError("Publication year cannot be in the future.")
        return year
