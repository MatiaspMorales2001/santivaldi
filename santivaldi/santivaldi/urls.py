"""
URL configuration for santivaldi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='IniciarSesion'),
    #cliente
    path('', views.index, name='index'),
    path('panaderia', views.panaderia),
    path('reposteria', views.reposteria),
    path('abarrotes', views.abarrotes),
    path('formulario', views.realizar_pedidos, name='pedido'),

    #Autentificacion
    path('IniciarSesion', views.iniciarSesion, name="inicio_sesion"),
    path('CerrarSesion', views.cerrarSesion),
    
    # JEFE
    path('registrar_trabajador', login_required(views.registrar_trabajador), name="registro"),
    path('trabajadores',login_required(views.ver_trabajadores),name='trabajador'),
    path('eliminar_trabajador/<rut>/', login_required(views.eliminar_trabajador), name="eliminar_trab"),
    path('modificar_trabajador/<rut>/', login_required(views.modificar_trabajador),name="modificar_trab"),
    path('detalle_producto', login_required(views.admin_productos)),

    #Administrador
    path('ingresar_producto', login_required(views.ingresar_producto)),
    path('productos', login_required(views.productos), name='productos_opciones'),
    path('eliminar_producto/<id>/', login_required(views.eliminar_producto), name="eliminar_prod"),
    path('modificar_producto/<id>/', login_required(views.modificar_producto),name="modificar_prod"),
    
    #vendedor
    path('ver_pedidos', login_required(views.ver_pedidos), name='pedidos'),
    path('ver_stock', login_required(views.stock)),
    path('modificar_estado/<id>/', login_required(views.modificar_estado), name="modificar_estados") ,

    
   


    
    
]
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

