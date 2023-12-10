from django import forms
from .models import Producto, Trabajador, Formulario
import re


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'precio', 'imagen', 'categoria', 'stock', 'fecha_vencimiento']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f'Ingrese {field.label}'





class ModificarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'precio', 'imagen', 'categoria','stock']  # Agrega cualquier otro campo que desees modificar
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f'Ingrese {field.label}'




class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['rut', 'nombre_trabajador', 'apellido_trabajador', 'email_trabajador', 'telefono_trabajador', 'rol', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),  # Usa el widget de contraseña para ocultar la entrada
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f'Ingrese {field.label}'

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not rut:
            self.add_error('rut', "Debe ingresar el RUT")

        # Validar el formato del RUT (xx.xxx.xxx-x o x.xxx.xxx-x) permitiendo números del 1 al 9
        # Después del guion, solo se aceptan números y una 'K'
        rut_pattern = re.compile(r'^[1-9]?\d{0,1}\.[1-9]\d{2}\.[1-9]\d{2}-[0-9kK]{1}$')
        if not rut_pattern.match(rut):
            self.add_error('rut', "Ingrese un RUT válido en el formato xx.xxx.xxx-x o x.xxx.xxx-x")

        return rut
    
    def clean_telefono_trabajador(self):
        telefono = self.cleaned_data.get('telefono_trabajador')
        if not telefono:
            self.add_error('telefono_trabajador', "Debe ingresar el teléfono")

        # Validar el formato del teléfono (9123456789)
        telefono_pattern = re.compile(r'^[1-9]\d{8}$')
        if not telefono_pattern.match(str(telefono)):
            self.add_error('telefono_trabajador', "Ingrese un teléfono válido en el formato 9123456789")

        return telefono
    

    def clean_email_trabajador(self):
        email = self.cleaned_data.get('email_trabajador')
        
        if not email:
            self.add_error_with_class('email_trabajador', "Debe ingresar un correo electrónico")

        # Validar el formato del correo electrónico
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$')
        if not email_pattern.match(email):
            self.add_error_with_class('email_trabajador', "Ingrese un correo electrónico válido")

        return email


class FormularioClienteForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nombre_cliente', 'apellido_cliente', 'telefono_cliente', 'pedido', 'estado']
        widgets = {
            'pedido': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Ingrese Pedido'}),
            'nombre_cliente': forms.TextInput(attrs={'placeholder': 'Ingrese Nombre'}),
            'apellido_cliente': forms.TextInput(attrs={'placeholder': 'Ingrese Apellido'}),
            'telefono_cliente': forms.TextInput(attrs={'placeholder': 'Ingrese Teléfono'}),
        }


class ModificarTrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = [ 'rol']
        widgets = {
            'contraseña': forms.PasswordInput(),  # Usa el widget de contraseña para ocultar la entrada
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = f'Ingrese {field.label}'

 

 