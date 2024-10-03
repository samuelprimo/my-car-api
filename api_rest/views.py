from django.shortcuts import render
from django.http import HttpReponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Veiculo
from .serializers import VeiculoSerializer

import json



@api_view(['GET'])
def get_users(request):
    
    if request.method == 'GET':
        veiculos = Veiculo.objects.all()

        serializer = VeiculoSerializer(veiculos, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_404_NOT_FOUND)


























# def databaseEmDjango():

#    data = Veiculo.objects.get()
#    data = Veiculo.objects.filter()
#    data = Veiculo.objects.exclude()

#    data.save()

#    data.delete()