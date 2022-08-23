from django.db import models
from clientes.models import Cliente

class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.IntegerField(max_length=70, null=False, blank=False)
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    balance = models.IntegerField('Balance', null=False, blank=False)
    iban = models.CharField('IBAN')

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        #Si se usa la base de datos del sprint 6
        #db_table = 'cuentas'

    def __str__(self):
        return self.account