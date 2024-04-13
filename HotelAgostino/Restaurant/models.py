from django.db import models
from django.utils import timezone

class Mesa(models.Model):
    Numero = models.IntegerField()
    Disponible = models.BooleanField(default=True)
    Capacidad = models.IntegerField()
    
class Reserva(models.Model):
    nombre_de_usuario = models.CharField(max_length=50)
    sala = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    
class Mesero(models.Model):
    pass

