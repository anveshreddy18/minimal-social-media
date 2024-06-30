from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.username

