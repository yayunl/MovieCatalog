from django.db import models

# Create your models here.
# app/movies/models.py

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass