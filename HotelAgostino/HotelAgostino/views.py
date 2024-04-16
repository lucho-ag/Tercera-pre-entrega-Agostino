from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Bienvenido a la página web de HotelAgostino</h1>")
    