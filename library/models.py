from django.db import models

from django.utils import timezone

class Book(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.author} | {self.title}'

class DVD(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    pegi = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return f'{self.title} | {self.duration}mn | {self.pegi} | {self.description}'