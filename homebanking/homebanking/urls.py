"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from clientes import views
from prestamos import views
from cuentas import views
from tarjetas import views
from login import views

urlpatterns = [
    path('clientes/', views.clientes, name="clientes"),
    path('cuentas/', views.cuentas, name="cuentas"),
    path('prestamos/', views.prestamos, name="prestamos"),
    path('tarjetas/', views.tarjetas, name="tarjetas"),
    path('login/', views.login, name="login"),
    path('admin/', admin.site.urls),
]
