from django.urls import path, include
from .views import home_view, ReservaCreateView, ReservaListView, ReservaDetailView, ReservaUpdateView, ReservaDeleteView, reserva_busqueda, MesaCreateView, MesaListView, MesaUpdateView, MesaDeleteView, mesa_busqueda, MeseroCreateView, MeseroListView, MeseroUpdateView, MeseroDeleteView

urlpatterns = [
    # RESERVA/
    path("", home_view),
    path("reserva/create", ReservaCreateView.as_view(), name="reserva-crear" ),
    path("reserva/list", ReservaListView.as_view(), name="reserva-lista"),
    path("reserva/<int:pk>/detail", ReservaDetailView.as_view(), name="reserva-detalle"),
    path("reserva/<int:pk>/update", ReservaUpdateView.as_view(), name="reserva-update"),
    path("reserva/<int:pk>/delete", ReservaDeleteView.as_view(), name="reserva-delete"),
    path("reserva/search", reserva_busqueda, name="reserva-search" ),
    
    # MESA/
    path("mesa/create", MesaCreateView.as_view(), name="mesa-crear"),
    path("mesa/list", MesaListView.as_view(), name="mesa-lista"),
    path("mesa/<int:pk>/update", MesaUpdateView.as_view(), name="mesa-update"),
    path("mesa/<int:pk>/delete", MesaDeleteView.as_view(), name="mesa-delete"),
    path("mesa/search", mesa_busqueda, name="mesa-search" ),

    # MESERO/
    path("mesero/create", MeseroCreateView.as_view(), name="mesero-crear"),
    path("mesero/list", MeseroListView.as_view(), name="mesero-lista"),
    path("mesero/<int:pk>/update", MeseroUpdateView.as_view(), name="mesero-update"),
    path("mesero/<int:pk>/delete", MeseroDeleteView.as_view(), name="mesero-delete"),
]


