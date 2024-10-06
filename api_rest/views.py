from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_modelo(request, modelo):

    try:
        veiculos = Veiculo.objects.get(modelo=modelo)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = VeiculoSerializer(veiculos)
        return Response(serializer.data)  


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def veiculo_manager(request):
    if request.method == 'GET':
        try:
            if 'placa' in request.GET:
                placa = request.GET['placa']
                try:
                    veiculo = Veiculo.objects.get(placa=placa)
                except Veiculo.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = VeiculoSerializer(veiculo)
                return Response(serializer.data)
            else:
                veiculos = Veiculo.objects.all()
                serializer = VeiculoSerializer(veiculos, many=True)
                return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    



    
        






















# def databaseEmDjango():

#    data = Veiculo.objects.get()
#    data = Veiculo.objects.filter()
#    data = Veiculo.objects.exclude()

#    data.save()

#    data.delete()