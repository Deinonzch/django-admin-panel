from django.db import models


class MyAdminPanel(models.Model):
    model_name = models.CharField(default='', blank=True, max_length=100)

    def __str__(self):
        return self.model_name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    date_of_birth = models.DateField('date of birth')

    def __str__(self):
        return self.second_name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    publishing_house = models.CharField(max_length=50)
    year = models.IntegerField(default=2000)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
