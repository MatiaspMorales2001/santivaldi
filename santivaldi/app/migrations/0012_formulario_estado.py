# Generated by Django 4.2.2 on 2023-12-08 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_formulario_alter_trabajador_telefono_trabajador'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('completo', 'Completo')], default='pendiente', max_length=20),
        ),
    ]