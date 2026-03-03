from django.db import models



# Author model stores author name
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book model stores title, year, and author reference
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
