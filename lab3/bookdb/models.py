from django.db import models


class Author(models.Model):
    AuthorID = models.CharField(primary_key=True,max_length=40)

    Name = models.CharField(max_length=40)
    Age = models.IntegerField()
    Country = models.CharField(max_length=40)

class Book(models.Model):
    ISBN = models.CharField(primary_key=True,max_length=40)
    Title = models.CharField(max_length=40)
    AuthorID = models.ForeignKey(Author,max_length=40)
    Publisher = models.CharField(max_length=40)
    PublishDate = models.DateField()
    Price = models.FloatField()
