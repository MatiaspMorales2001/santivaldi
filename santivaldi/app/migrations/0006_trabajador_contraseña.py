# Generated by Django 4.2.2 on 2023-12-06 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_trabajador'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='contraseña',
            field=models.CharField(default='', max_length=255),
        ),
    ]
