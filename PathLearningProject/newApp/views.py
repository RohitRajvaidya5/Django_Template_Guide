from django.shortcuts import render

# Create your views here.

def all_temp(request):
    return render (request, 'newApp/all_temp.html')
