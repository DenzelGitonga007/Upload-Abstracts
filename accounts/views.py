from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # For user creation
from django.contrib import messages # For alert messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! Your account is successfully registered. You can now log in...")
            return redirect('login') # Redirect to login page
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request, 'accounts/register.html', context)
