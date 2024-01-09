from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    """Manages the user creation"""
    def create_user(self, email, username, password=None, **extra_fields):
        """Create the normal user"""
        # Get the email importantly
        if not email:
            raise ValueError("Please provide an email address")
        email = self.normalize_email(email) # for case sensitivity issues with email
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractUser):
    """Get the user's details for creation"""
    username = models.TextField(max_length=25, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=14)

    # get the full_name of user 
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    objects = CustomUserManager()