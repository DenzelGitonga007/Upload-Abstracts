from django.db import models
from accounts.models import CustomUser

# Create your models here.

# File path
def abstract_file_path(instance, filename):
    """Upload file to the 'abstracts/username' subdirectory"""
    return "abstracts/{}/{}".format(instance.author.username, filename)

class Abstract(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField(max_length=254)
    file = models.FileField(upload_to=abstract_file_path, null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} {}".format(self.title, self.author, self.file)
