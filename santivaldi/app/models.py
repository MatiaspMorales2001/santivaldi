from django.db import models
import os
from django.contrib.auth.models import User
from django.utils import timezone
import random
from datetime import timedelta
# Create your models here.

def get_upload_path(instance, filename):
    # Obtener la categoría del producto
    categoria = instance.categoria
    # Crear la ruta de almacenamiento basada en la categoría
    return os.path.join("productos", categoria, filename)

class Producto(models.Model):
    CATEGORIAS_CHOICES = [
        ('reposteria', 'Reposteria'),
        ('panaderia', 'Panadería'),
        ('abarrotes', 'Abarrotes'),
    ]

    idproducto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=45, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    imagen = models.ImageField(upload_to=get_upload_path, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES)
    stock = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateTimeField(default=timezone.now)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre_producto

    def generar_fecha_vencimiento(self):
        # Generar un número de meses al azar (entre 1 y 12)
        meses_al_azar = random.randint(1, 12)

        # Calcular la nueva fecha de vencimiento sumando meses al actual
        nueva_fecha_vencimiento = self.fecha_ingreso + timedelta(days=30 * meses_al_azar)

        return nueva_fecha_vencimiento

    def save(self, *args, **kwargs):
        # Si la fecha de vencimiento no se estableció, generamos una al guardar el producto
        if not self.fecha_vencimiento:
            self.fecha_vencimiento = self.generar_fecha_vencimiento()

        super().save(*args, **kwargs)
    

class Trabajador (models.Model):
    categorias_choices = [
        ('Administrador', 'administrador'),
        ('Vendedor', 'vendedor'),
        
    ]
    rut = models.CharField(max_length=12, primary_key=True)
    nombre_trabajador = models.CharField(max_length=25, blank=True, null=True)
    apellido_trabajador = models.CharField(max_length=25, blank=True, null=True)
    email_trabajador = models.CharField(max_length=100, blank=True, null=True)
    telefono_trabajador = models.CharField(max_length=9,blank=True, null=True)
    rol = models.CharField(max_length=20, choices=categorias_choices)
    contraseña = models.CharField(max_length=255, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self) -> str:
        return self.nombre_trabajador
    

class Formulario(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completo', 'Completo'),
    ]

    id_formulario = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=25, blank=True, null=True)
    apellido_cliente = models.CharField(max_length=25, blank=True, null=True)
    telefono_cliente = models.CharField(max_length=9, blank=True, null=True)    
    pedido = models.CharField(max_length=450, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True,choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f'Formulario-{self.id_formulario} ({self.nombre_cliente} {self.apellido_cliente})'

    