from django.db import models
from django.apps import AppConfig

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField('Nombre', max_length=255, blank=False, null=False)
    customer_surname = models.TextField('Apellido', max_length=255, blank=False, null=False)  # This field type is a guess.
    customer_dni = models.TextField('DNI', max_length=8, db_column='customer_DNI', blank=False, null=False)  # Field name made lowercase.
    dob = models.TextField('Fecha de nacimiento', blank=False, null=False)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.customer_id


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

