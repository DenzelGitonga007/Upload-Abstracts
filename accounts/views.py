from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm # Login form
from django.contrib.auth import authenticate, login, logout # For authentication
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
    if user.is_authenticated and not user.is_anonymous:
        if user.is_superuser:
            abstracts = Abstract.objects.all()
        else:
            abstracts = Abstract.objects.filter(author=user)
    else:
        abstracts = Abstract.objects.none()  # To handle the anonymous user error
    context = {
        'user': user,
        'abstracts': abstracts
        }
    return render(request, "index.html", context)

# Logout
def user_logout(request):
    """Logout"""
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have successfully logged out...")
        return redirect("accounts:home")
    context = {}
    return render(request, "accounts/logout.html", context)


