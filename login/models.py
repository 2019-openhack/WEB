from django.db import models

# Create your models here.

class Dic(models.Model):
    word = models.CharField(max_length=100)
    mean = models.CharField(max_length=100)
    sentence = models.CharField(max_length=100)
    pron = models.CharField(max_length=100)
    remind = models.PositiveIntegerField(default=4)


class User(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(max_length=70, default="ajs7270@naver.com")
    dic = models.ManyToManyField(Dic)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.user_name
 
