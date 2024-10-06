from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'),
    path('modelo/<str:modelo>', views.get_by_modelo),
    path('data/', views.veiculo_manager) 
    
    
]
