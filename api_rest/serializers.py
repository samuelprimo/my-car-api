from rest_framework import serializers

from .models import Veiculo


class VeiculoSerializer(serializers.ModelSerialiazer):
    class Meta:
        model = Veiculo
        fields = '__all__'
