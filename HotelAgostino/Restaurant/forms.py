from django import forms

from .models import Reserva, Mesa, Mesero

class ReservaSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingresar nombre de usuario")
    
class MesaSearchForm(forms.Form):
    numero = forms.IntegerField(required=True, label="Ingresar numero de mesa")