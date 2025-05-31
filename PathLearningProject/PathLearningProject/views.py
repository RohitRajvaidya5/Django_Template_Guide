from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, This is home.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is the contact page")
            