# Generated by Django 4.0.6 on 2022-09-06 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='dob',
        ),
    ]
