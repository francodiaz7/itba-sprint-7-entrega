from django.shortcuts import render
from .models import Cliente

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request,"clientes/clientes.html", {'clientes':clientes})