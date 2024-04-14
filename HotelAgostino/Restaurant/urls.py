from django.urls import path, include
from .views import home_view, ReservaCreateView

urlpatterns = [
    path("", home_view),
    path("crear-reserva", ReservaCreateView, name="crear-reserva" )
]