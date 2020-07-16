from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, "test/test.html")

def modelo(request):
    return render(request, "modelo.html")

def formulario(request):
    return render(request, "formulario.html")

def iniciar(request):
    
    return render(request, "inicio.html")

