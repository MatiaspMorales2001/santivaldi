from django.shortcuts import render, redirect, get_object_or_404
from app.models import Producto, Trabajador, Formulario
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.contrib.auth.models import User
from .forms import ProductoForm, TrabajadorForm, FormularioClienteForm,ModificarTrabajadorForm
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

#FUNCIONES PARA LOS USUARIOS NORMALES
def index(request):
    return render(request, "app/index.html")



def panaderia(request):
    prod = Producto.objects.all()
    data = {"app_producto":prod}
    return render(request, "app/panaderia.html",data)

def reposteria(request):
    prod = Producto.objects.all()
    data = {"app_producto":prod}
    return render(request, "app/reposteria.html",data)

def abarrotes(request):
    prod = Producto.objects.all()
    data = {"app_producto":prod}
    return render(request, "app/abarrotes.html",data)


def realizar_pedidos(request):
    if request.method == 'POST':
        form = FormularioClienteForm(request.POST)
        if form.is_valid():
            # Guardar el formulario
            form.save()
            return redirect('index')
    else:
        form = FormularioClienteForm()

    return render(request, 'cliente/realizar_pedidos.html', {'form': form})



# AUTENTIFICACION
def iniciarSesion(request):
    # Redirigir si ya está autenticado
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        usuario = request.POST.get('usernameOrEmail')
        contraseña = request.POST.get('password')
        user = authenticate(request, username=usuario, password=contraseña)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, inténtalo de nuevo.')

    return render(request, 'autentificacion/iniciarSesion.html')


def cerrarSesion(request):
    logout(request)
    return redirect("index")



#Funciones del jefe
@login_required
def registrar_trabajador(request):
    form = None
    if request.method == "POST":
        try:
            form = TrabajadorForm(request.POST)
            if form.is_valid():
                with transaction.atomic():
                    usuario = form.save(commit=False)  # guardar modelo usuario en la base de datos
                    # crear usuario django
                    user = User.objects.create_user(
                        form.cleaned_data['email_trabajador'],
                        form.cleaned_data['email_trabajador'],
                        form.cleaned_data['contraseña']
                    )

                    if form.cleaned_data['rol'] == 'administrador' or form.cleaned_data['rol'] == 'Administrador':
                        user.is_staff = True
                        user.is_superuser = False
                    elif form.cleaned_data['rol'] == 'vendedor' or form.cleaned_data['rol'] == 'Vendedor':
                        user.is_staff = False
                        user.is_superuser = False
                    
                    user.first_name = form.cleaned_data['nombre_trabajador']
                    user.last_name = form.cleaned_data['apellido_trabajador']
                    user.email = form.cleaned_data['email_trabajador']
                    user.save() 
                    usuario.user = user
                    usuario.save()
                    return redirect('index')
        except ValidationError as e:
            for field, error_list in e.message_dict.items():
                for error in error_list:
                    messages.error(request, f'{field}:{error}')
        except Exception as e:
            print(e)
            messages.error(request, 'ERROR EN EL REGISTRO, Inténtelo nuevamente')

    else:
        form = TrabajadorForm()
    return render(request, 'jefe/registrar_trabajador.html', {'form': form})


@login_required
def ver_trabajadores(request):
    trabajadores = Trabajador.objects.all()
    data = {'trabajadores': trabajadores}
    return render(request, 'jefe/ver_trabajadores.html',data)

@login_required
def eliminar_trabajador(request, rut):
    trabajador = get_object_or_404(Trabajador, rut=rut)
    
    # Eliminar el usuario de Django asociado al trabajador si existe
    user = trabajador.user
    if user:
        user.delete()

    # Eliminar el trabajador
    trabajador.delete()

    return redirect('trabajador')

@login_required
def modificar_trabajador(request, rut):
    trabajador = get_object_or_404(Trabajador, rut=rut)

    if request.method == 'POST':
        form = ModificarTrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            user = trabajador.user  # Obtener el usuario asociado al trabajador
            if form.cleaned_data['rol'].lower() == 'administrador':
                user.is_staff = True
                user.is_superuser = False
            elif form.cleaned_data['rol'].lower() == 'vendedor':
                user.is_staff = False
                user.is_superuser = False
            user.save()  # Guardar los cambios en el usuario
            form.save()
            return redirect('trabajador')  # Redirigir a la página de trabajadores después de modificar el rol
    
    else:
        form = ModificarTrabajadorForm(instance=trabajador)

    return render(request, 'jefe/modificar_trabajador.html', {'form': form, 'trabajador': trabajador})


@login_required
def admin_productos(request):
    prod = Producto.objects.all
    data = {'app_producto':prod}
    return render(request, 'jefe/detalle_producto.html', data)




# Funciones del administrador
@login_required
def ingresar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ProductoForm()

    return render(request, 'administrador/ingresar_producto.html', {'form': form})

@login_required
def productos(request):
    prod = Producto.objects.all
    data = {'app_producto':prod}
    return render(request, 'administrador/opcion_productos.html', data)

@login_required
def eliminar_producto(request, id):
    prod = get_object_or_404(Producto, idproducto=id)
    prod.delete()
    return redirect("productos_opciones")

@login_required
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, idproducto=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos_opciones') 
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'administrador/modificar_producto.html', {'form': form, 'producto': producto})




# Funciones del vendedor
@login_required
def ver_pedidos(request):
    pedidos = Formulario.objects.all()
    data = {'pedidos':pedidos}
    return render(request, 'vendedor/ver_pedidos.html', data)
@login_required
def stock(request):
    stock = Producto.objects.all
    data = {'app_producto':stock}
    return render(request, 'vendedor/ver_stock.html', data)

@login_required
def modificar_estado(request, id):
    formulario = get_object_or_404(Formulario, id_formulario=id)

    if request.method == 'POST':
        form = FormularioClienteForm(request.POST, instance=formulario)
        if form.is_valid():
            form.save()
            # redirigir a otra página después de guardar el formulario
            return redirect('pedidos')

    else:
        form = FormularioClienteForm(instance=formulario)

    return render(request, 'vendedor/modificar_estado.html', {'form': form})


