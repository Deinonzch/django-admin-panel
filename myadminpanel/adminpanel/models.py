from django.db import models
from django.apps import apps


class MyAdminPanel(models.Model):
    model_name = models.CharField(default='', blank=False, max_length=100)
    app_name = models.CharField(default='', blank=False, max_length=100)

    def __str__(self):
        return self.model_name

    def save(self, *args, **kwargs):
        self.model_name = self.model_name.lower()
        self.app_name = self.app_name.lower()
        return super(MyAdminPanel, self).save(*args, **kwargs)

    @staticmethod
    def get_model(app, model):
        return apps.get_model(app, model)


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
