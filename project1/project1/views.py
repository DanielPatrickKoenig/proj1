# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('Hi there dude')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('about time.')
    return render(request, 'about.html')