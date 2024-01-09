from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm # Login form
from django.contrib.auth import authenticate, login # For login
from django.contrib import messages # For alert messages
from .forms import CustomUserCreationForm
from abstracts.models import Abstract # Get the abstracts
# Create your views here.

# register
def register(request):
    """Register user"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! Your account is successfully registered. You can now log in...")
            return redirect('accounts:login') # Redirect to login page
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

# Login
def user_login(request):
    """Login user"""
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Welcome {}! You're now logged in.", format(username))
                return redirect('accounts:home')
            else:
                messages.error(request, "Oops! Login error...Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, "accounts/login.html", context)

# Home
def home(request):
    """Landing page"""
    user = request.user
    abstracts = Abstract.objects.filter(author=user)
    context = {
        'user': user,
        'abstracts': abstracts
        }
    return render(request, "index.html", context)


