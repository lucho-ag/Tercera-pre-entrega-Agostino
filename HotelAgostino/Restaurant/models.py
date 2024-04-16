from django.db import models
from django.utils import timezone

class Mesa(models.Model):
    numero = models.IntegerField()
    disponible = models.BooleanField(default=True)
    capacidad = models.IntegerField()
    
    def __str__(self):
        return f"Mesa: {self.numero} - {'Disponible' if self.disponible else 'No Disponible'} - Capacidad: {self.capacidad}"
    
class Reserva(models.Model):
    nombre_de_usuario = models.CharField(max_length=50)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.nombre_de_usuario} - Mesa:{self.mesa.numero} - {self.fecha}"
    
class Mesero(models.Model):
    nombre = models.CharField(max_length=50)
    mesa_asignada = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='meseros')
    
    def __str__(self):
        return f"{self.nombre} - Asignado mesa: {self.mesa_asignada.numero}"

