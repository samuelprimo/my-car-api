from django.db import models

class Veiculo(models.Model):
    placa = models.CharField(max_length=10, primary_key=True, default='')
    marca = models.CharField(max_length=50, default='')
    modelo = models.CharField(max_length=50, default='')
    ano = models.IntegerField(default=0)
    cor = models.CharField(max_length=20, default='')
    quilometragem = models.IntegerField(default=0)
    combustivel = models.CharField(max_length=20, choices=[
        ('gasolina', 'Gasolina'),
        ('etanol', 'Etanol'),
        ('diesel', 'Diesel'),
        ('eletrico', 'Elétrico'),
        ('hibrido', 'Híbrido'),
    ], default='gasolina')
    proprietario = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'Placa: {self.placa} | Marca: {self.marca} | Modelo: {self.modelo}'