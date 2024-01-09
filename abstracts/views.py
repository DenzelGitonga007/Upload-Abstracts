from django.shortcuts import render, get_object_or_404, redirect
from .models import Abstract
from .forms import AbstractForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages # Display messages


# Create your views here.
# Create
@login_required(login_url="accounts:login")
def abstract_create(request):
    """Upload abstract"""
    if request.method == "POST":
        form = AbstractForm(request.POST, request.FILES)
        if form.is_valid():
            abstract = form.save(commit=False)
            abstract.author = request.user
            abstract.save()
            messages.success(request, "Abstract uploaded successfully.")
            return redirect('accounts:home')
    else:
        form = AbstractForm()
    context = {'form': form}
    return render(request, "abstracts/upload.html", context)
        
# Edit
@login_required
def abstract_edit(request, pk):
    abstract = get_object_or_404(Abstract, pk=pk)
    if request.method == "POST":
        form = AbstractForm(request.POST, request.FILES, instance=abstract)
        if form.is_valid():
            form.save()
            messages.success(request, "Abstract updated successfully...")
            return redirect("accounts:home")
    else:
        form = AbstractForm(instance=abstract)
    context = {'form': form}
    return render(request, "abstracts/edit.html", context)