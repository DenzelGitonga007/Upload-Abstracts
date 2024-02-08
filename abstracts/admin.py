from django.contrib import admin
from django.utils.html import format_html
from .models import Abstract

class AbstractAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_file_link']
    search_fields = ['title', 'author', 'file', 'description']

    def display_file_link(self, obj):
        if obj.file:
            file_url = obj.file.url
            return format_html(f'<a href="{file_url}" download>Download</a>')
        return "No File"

    display_file_link.short_description = "Download File"

admin.site.register(Abstract, AbstractAdmin)
