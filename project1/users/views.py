from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def register_user (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("/posts")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', { 'form': form })

def login_user (request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/posts")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', { 'form': form })

# Create your views here.
