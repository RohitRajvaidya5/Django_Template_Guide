
from django.urls import path, include
from . import views

urlpatterns = [
   
   path('', views.all_temp, name= 'all_temp')
    
]