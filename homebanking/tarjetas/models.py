from django.db import models
from ..clientes.models import Cliente

# Create your models here.
class Tarjeta(models.Model):
    numero = models.IntegerField(verbose_name='Número', max_length=20)
    CVV = models.IntegerField(verbose_name='CVV', max_length=3)
    fecha_de_otorgamiento = models.DateTimeField()
    fecha_de_vencimiento = models.DateTimeField()
    tipo_tarjeta = models.CharField(verbose_name='Tipo de tarjeta', max_length=10)
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        manage = True
        db_table = 'tarjeta'