from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.CharField(max_length=100)
    example = models.CharField(max_length=100)

