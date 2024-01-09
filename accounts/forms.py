from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .import models

class CustomUserCreationForm(UserCreationForm):
    """Custom form for user creation"""
    email = forms.EmailField(required=True)

    class Meta:
        model = models.CustomUser
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove autofocus attribute
        self.fields["username"].widget.attrs.pop("autofocus", None)
