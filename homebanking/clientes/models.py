from django.db import models

# Create your models here.
class Cliente(models.Model):
    customer = models.IntegerField(primary_key=True)
    customer_name = models.CharField(verbose_name='Nombre', max_length=70)
    customer_surname = models.CharField(verbose_name='Apellido', max_length=70)
    customer_DNI = models.IntegerField(verbose_name='DNI', max_length=10)
    dob = models.DateField(verbose_name='Fecha de nacimiento')

    class Meta:
        managed = True
        db_table = 'cliente'
