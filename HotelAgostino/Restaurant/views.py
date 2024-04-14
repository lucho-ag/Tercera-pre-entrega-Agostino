from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Mesa, Reserva, Mesero


def home_view(request):
    return render(request, "Restaurant/home.html")

class ReservaCreateView(CreateView):
    model = Reserva
    template_name = 'Restaurant/reserva_form.html'
    fields = ['nombre', 'mesa', 'fecha', "hora de inicio"]
    success_url = reverse_lazy('')

    
    
