# Generated by Django 4.0.6 on 2022-09-06 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamos_tabla',
            fields=[
                ('loan_id', models.AutoField(default='', primary_key=True, serialize=False)),
                ('loan_type', models.TextField(default='name_cliente', max_length=30, verbose_name='Tipo de préstamo')),
                ('loan_date', models.TextField(verbose_name='Fecha')),
                ('loan_total', models.IntegerField(verbose_name='Total')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.cliente')),
            ],
            options={
                'verbose_name': 'Préstamo',
                'verbose_name_plural': 'Préstamos',
            },
        ),
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('loan_id', models.AutoField(default='', primary_key=True, serialize=False)),
                ('loan_type', models.TextField(default='name_cliente', max_length=30, verbose_name='Tipo de préstamo')),
                ('loan_date', models.TextField(verbose_name='Fecha')),
                ('loan_total', models.IntegerField(verbose_name='Total')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.cliente')),
            ],
            options={
                'verbose_name': 'Préstamo',
                'verbose_name_plural': 'Préstamos',
                'db_table': 'prestamos',
            },
        ),
    ]
