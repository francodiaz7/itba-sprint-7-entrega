from django.db import models

# Create your models here.
class Empleado(models.Model):
    empleado_id=models.AutoField(primary_key=True)
    empleado_name=models.TextField('Nombre', max_length=255, null=False, blank=False)
    empleado_apellido=models.TextField('Apellido', max_length=255, null=False, blank=False)
    empleado_fecha_nacimiento=models.DateField('Fecha de nacimiento', null=False, blank=False)
    empleado_DNI=models.IntegerField('DNI', max_length=8, null=False, blank=False)