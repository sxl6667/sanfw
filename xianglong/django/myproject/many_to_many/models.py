from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=16)
    def __str__(self):
        return self.name


class Music(models.Model):
    title = models.CharField(max_length=16)
    author = models.ManyToManyField(Author)
    def __str__(self):
        return self.title