from django.db import models

class Cliente(models.Model):
    customer = models.AutoField(primary_key=True)
    customer_name = models.CharField('Nombre', max_length=255, null=False, blank=False)
    customer_surname = models.CharField('Apellido', max_length=255, null=False, blank=False)
    customer_DNI = models.IntegerField('DNI', max_length=8, null=False, blank=False)
    dob = models.DateField('Fecha de nacimiento', null=False, blank=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        #Si se usa la base de datos del sprint 6
        # db_table = 'clientes'

    def __str__(self):
        return self.customer
