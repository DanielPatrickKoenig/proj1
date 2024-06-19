from django.shortcuts import render

def register_user (request):
    return render(request, 'users/register.html')

# Create your views here.
