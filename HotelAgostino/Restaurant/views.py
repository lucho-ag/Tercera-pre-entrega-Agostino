from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Mesa, Reserva, Mesero
from .forms import ReservaSearchForm, MesaSearchForm

def home_view(request):
    return render(request, "Restaurant/home.html")

# --------------------RESERVAS--------------------

class ReservaCreateView(CreateView):
    model = Reserva
    template_name = 'Restaurant/reserva_form.html'
    fields = ['nombre_de_usuario', 'mesa', 'fecha', "hora_inicio"]
    success_url = reverse_lazy('reserva-lista')
    
class ReservaListView(ListView):
    model = Reserva
    template_name = 'Restaurant/reserva_list.html'
    context_object_name = 'reservas'

class ReservaDetailView(DetailView):
    model = Reserva
    template_name = 'Restaurant/reserva_detail.html'
    context_object_name = 'reserva'

class ReservaUpdateView(UpdateView):
    model = Reserva
    template_name = 'Restaurant/reserva_form.html'
    fields = ['nombre_de_usuario', 'mesa', 'fecha', "hora_inicio"]
    context_object_name = 'reserva'
    success_url = reverse_lazy('reserva-lista')

class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'Restaurant/reserva_delete.html'
    success_url = reverse_lazy('reserva-lista')

def reserva_busqueda(request):
    if request.method == "GET":
        form = ReservaSearchForm
        return render(request, "Restaurant/reserva_busqueda.html", context={"search_form": form })
    elif request.method == "POST":
        form = ReservaSearchForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
        reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
        contexto_dict = {"reservas": reservas_del_usuario}
        return render(request, "Restaurant/reserva_list.html", contexto_dict)
    
# --------------------MESAS--------------------

class MesaCreateView(CreateView):
    model = Mesa
    template_name = 'Restaurant/mesa_form.html'
    fields = ['numero', 'disponible', 'capacidad']
    success_url = reverse_lazy('mesa-lista')
    
class MesaListView(ListView):
    model = Mesa
    template_name = 'Restaurant/mesa_list.html'
    context_object_name = 'mesas'

class MesaUpdateView(UpdateView):
    model = Mesa
    template_name = 'Restaurant/mesa_form.html'
    fields = ['numero', 'disponible', 'capacidad']
    context_object_name = 'mesa'
    success_url = reverse_lazy('mesa-lista')

class MesaDeleteView(DeleteView):
    model = Mesa
    template_name = 'Restaurant/mesa_delete.html'
    success_url = reverse_lazy('mesa-lista')
    
def mesa_busqueda(request):
    if request.method == "GET":
        form = MesaSearchForm
        return render(request, "Restaurant/mesa_busqueda.html", context={"search_form": form })
    elif request.method == "POST":
        form = MesaSearchForm(request.POST)
        if form.is_valid():
            numero = form.cleaned_data['numero']
        mesas = Mesa.objects.filter(numero=numero).all()
        contexto_dict = {"mesas": mesas}
        return render(request, "Restaurant/mesa_list.html", contexto_dict)
    
# --------------------MESEROS--------------------

class MeseroCreateView(CreateView):
    model = Mesero
    template_name = 'Restaurant/mesero_form.html'
    fields = ['nombre', 'mesa_asignada']
    success_url = reverse_lazy('mesero-lista')
    
class MeseroListView(ListView):
    model = Mesero
    template_name = 'Restaurant/mesero_list.html'
    context_object_name = 'meseros'

class MeseroUpdateView(UpdateView):
    model = Mesero
    template_name = 'Restaurant/mesero_form.html'
    fields = ['nombre', 'mesa_asignada']
    context_object_name = 'mesero'
    success_url = reverse_lazy('mesero-lista')

class MeseroDeleteView(DeleteView):
    model = Mesero
    template_name = 'Restaurant/mesero_delete.html'
    success_url = reverse_lazy('mesero-lista')
