from django.contrib import admin
from .models import Abstract

# Register your models here.
class AbstractAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'file']
    search_fields = ['title', 'author', 'file', 'description']

admin.site.register(Abstract, AbstractAdmin)
