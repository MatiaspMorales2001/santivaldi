# Generated by Django 4.2.2 on 2023-12-06 23:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_trabajador_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fecha_ingreso',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
