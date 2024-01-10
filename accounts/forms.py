from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


# Registration Form
class CustomUserCreationForm(UserCreationForm):
    """Custom form for user creation"""
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    # Unique email
    def clean_email(self):
        """Ensure email is unique at form level"""
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use")
        return email


    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove autofocus attribute
        self.fields["username"].widget.attrs.pop("autofocus", None)

# Login Form
# class CustomLoginForm(forms.ModelForm):
#     username = forms.CharField(label="username", max_length=100)
#     password = forms.CharField(label="password", widget=forms.PasswordInput())