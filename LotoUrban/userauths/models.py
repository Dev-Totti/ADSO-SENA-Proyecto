from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Remove username field
    username = None

    # Add email field
    email = models.EmailField(unique=True, null=False, blank=False)

    # Make email field as the USERNAME_FIELD
    USERNAME_FIELD = "email"

    # Add required fields
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

