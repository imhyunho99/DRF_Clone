from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

# models.py
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title



