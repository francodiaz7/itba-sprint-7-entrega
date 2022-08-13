from django.db import models
from ..clientes.models import Cliente

# Create your models here.
class Cuenta(models.Model):
    account = models.IntegerField(primary_key=True, verbose_name='Cuenta')
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    balance = models.IntegerField(verbose_name='Balance')
    iban = models.CharField(verbose_name='IBAN')

    class Meta:
        manage = True
        db_table = 'cuenta'