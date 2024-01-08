from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.TextField(max=25)
    email = models.EmailField(max=50)
    phone = models.CharField(max=14)
    