from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
