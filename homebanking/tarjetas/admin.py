from django.contrib import admin
from .models import MarcasDeTarjetas, Tarjeta

admin.site.register(Tarjeta, MarcasDeTarjetas)