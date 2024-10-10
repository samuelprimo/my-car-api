from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('veiculos/', views.get_veiculos),
    path('modelo/<str:modelo>', views.get_by_modelo),
    path('data/', views.veiculo_manager) 
    
    
]
