from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.TextField(max=25)
    email = models.EmailField(max=50)
    phone = models.CharField(max=14)

    # get the full_name of user 
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)