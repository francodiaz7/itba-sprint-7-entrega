from django.db import models
from django.apps import AppConfig
from django.contrib.auth.models import User

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField('Nombre', max_length=255, null=False, blank=False)
    customer_surname = models.CharField('Apellido', max_length=255, null=False, blank=False)
    customer_DNI = models.IntegerField('DNI', null=False, blank=False)
    dob = models.DateField('Fecha de nacimiento', null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.customer_name


class DireccionCliente(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    direccion = models.TextField('Dirección', max_length=255, blank=False, null=False)
    ciudad = models.TextField('Ciudad', max_length=255, blank=False, null=False)
    provincia = models.TextField('Provincia', max_length=255, blank=False, null=False)
    pais = models.TextField('País', max_length=255, blank=False, null=False)
    customer_id = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'direcciones'
        verbose_name = 'Dirección del cliente'
        verbose_name_plural = 'Direcciones del cliente'


class TipoCliente(models.Model):
    tipo_cliente_id = models.AutoField(primary_key=True)
    tipos_de_clientes = models.TextField('Tipo de cliente', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'tipo_cliente'
        verbose_name = 'Tipo de cliente'
