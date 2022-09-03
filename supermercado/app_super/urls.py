from django.urls import path
from app_super.views import *


urlpatterns = [
    path('inicio/', inicio),
    path('add_proveedor/', proveedor_form, name="add_proveedor"), # los "name" son para colocar en los botones, en las html's
    path('buscar_proveedor/', buscar_proveedor, name="buscar_proveedor"),
    path('buscar_prov/', buscar_prov, name="buscar_prov"),
    path('ver_proveedores/', ver_proveedores, name="ver_proveedores"),
    path('add_empleado/', empleado_form, name="add_empleado"),
    path('buscar_empleado/', buscar_empleado, name="buscar_empleado"),
    path('buscar_emp/', buscar_emp, name="buscar_emp"),
    path('ver_empleados/', ver_empleados, name="ver_empleados"),
    path('add_cliente/', cliente_form, name="add_cliente"),
    path('buscar_cliente/', buscar_cliente, name="buscar_cliente"),
    path('buscar_cli/', buscar_cli, name="buscar_cli"),
    path('ver_clientes/', ver_clientes, name="ver_clientes"),
]