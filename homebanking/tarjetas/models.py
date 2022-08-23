from django.db import models
from clientes.models import Cliente

class Tarjeta(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField(max_length=20)
    CVV = models.IntegerField('CVV', max_length=3)
    fecha_de_otorgamiento = models.DateTimeField('Fecha de otorgamiento')
    fecha_de_vencimiento = models.DateTimeField('Fecha de vencimiento')
    tipo_tarjeta = models.CharField('Tipo de tarjeta', max_length=10)
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'
        #Si se usa la base de datos del sprint 6
        #db_table = 'tarjeta'

    def __str__(self):
        return self.numero