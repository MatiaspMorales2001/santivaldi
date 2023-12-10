from django.contrib import admin
from .models import Producto,Trabajador, Formulario
# Register your models here.
admin.site.register(Producto)
admin.site.register(Trabajador)
admin.site.register(Formulario)