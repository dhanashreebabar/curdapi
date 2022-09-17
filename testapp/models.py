from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    lsbn = models.CharField(max_length=60)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.title

