from django.db import models
from clientes.models import Cliente

class Prestamos(models.Model):
    loan = models.IntegerField(primary_key=True)
    loan_type = models.CharField('Tipo de préstamo', max_length=70, null=False, blank=False)
    loan_date = models.DateField('Fecha')
    loan_total = models.IntegerField('Monto', max_length=70, null=False, blank=False)
    customer = models.IntegerField(Cliente, models.DO_NOTHING)

    class Meta:
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'
        #Si se usa la base de datos del sprint 6
        #db_table = 'prestamo'

    def __str__(self):
        return self.loan