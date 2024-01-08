from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.TextField(max_length=25, unique=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=14)

    # get the full_name of user 
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)