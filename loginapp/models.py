from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
