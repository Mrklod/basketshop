from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    phone = models.CharField(max_length=50,unique=True)
    photo = models.ImageField(blank=True,upload_to='profile')