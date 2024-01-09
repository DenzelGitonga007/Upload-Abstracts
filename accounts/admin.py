from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomuserAdmin(admin.ModelAdmin):
    """Customize admin interface for accounts, CustomUser model"""
    list_display = ["username", "email", "phone", "is_staff"]
    search_fields = ["username", "email"]

admin.site.register(CustomUser, CustomuserAdmin)