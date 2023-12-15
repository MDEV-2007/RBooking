from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_prictute', default='profile_picture.jpeg')