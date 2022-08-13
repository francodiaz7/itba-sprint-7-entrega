from django.db import models
from ..clientes.models import Cliente

# Create your models here.
class Prestamos(models.Model):
    loan = models.IntegerField(primary_key=True)
    loan_type = models.CharField(verbose_name='Tipo de préstamo', max_length=20)
    loan_date = models.DateField(verbose_name='Fecha')
    loan_total = models.IntegerField(verbose_name='Monto', max_length=20)
    customer = models.IntegerField(Cliente, models.DO_NOTHING)

    class Meta:
        manage = True
        db_table = 'prestamo'