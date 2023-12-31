# Generated by Django 4.2.2 on 2023-12-18 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_formulario_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='formulario',
            name='estado',
            field=models.CharField(blank=True, choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('completo', 'Completo')], default='pendiente', max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(through='app.ItemCarrito', to='app.producto'),
        ),
        migrations.AddField(
            model_name='formulario',
            name='carrito',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.carrito'),
        ),
    ]
