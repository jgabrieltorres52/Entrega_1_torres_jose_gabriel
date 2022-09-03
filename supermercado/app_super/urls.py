from django.urls import path
from app_super.views import *


urlpatterns = [
    path('inicio/', inicio),
    path('add_proveedor/', proveedor_form, name="add_proveedor"), # los "name" son para colocar en los botones, en las html's
    path('busqueda_proveedor/', busqueda_proveedor, name="busqueda_proveedor"),
    path('buscar_proveedor/', buscar_proveedor, name="buscar_proveedor"),
    path('ver_proveedores/', ver_proveedores, name="ver_proveedores"),
    path('add_empleado/', empleado_form, name="add_empleado"),
    path('busqueda_empleado/', busqueda_empleado, name="busqueda_empleado"),
    path('buscar_empleado/', buscar_empleado, name="buscar_empleado"),
    path('ver_empleados/', ver_empleados, name="ver_empleados"),
    path('add_cliente/', cliente_form, name="add_cliente"),
    path('busqueda_cliente/', busqueda_cliente, name="busqueda_cliente"),
    path('buscar_cliente/', buscar_cliente, name="buscar_cliente"),
    path('ver_clientes/', ver_clientes, name="ver_clientes"),
]