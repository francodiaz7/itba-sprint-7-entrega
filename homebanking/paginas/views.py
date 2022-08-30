from django.shortcuts import render

# Create your views here.
def atencion_clientes(request):
    return render(request, 'paginas/atencion_cliente.html')