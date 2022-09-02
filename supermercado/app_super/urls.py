from django.urls import path
from app_super.views import *


urlpatterns = [
    path('inicio/', inicio),
    path('add_proveedor/', proveedor_form, name="add_prov"), # los "name" son para colocar en los botones, en las html's
    path('buscar_proveedor/', buscar_proveedor, name="buscar_prov"),
    path('ver_proveedores/', ver_proveedores, name="ver_prov"),
    path('add_empleado/', empleado_form, name="add_emp"),
    path('buscar_empleado/', buscar_empleado, name="buscar_emp"),
    path('ver_empleados/', ver_empleados, name="ver_emp"),
    path('add_cliente/', cliente_form, name="add_cli"),
    path('buscar_cliente/', buscar_cliente, name="buscar_cli"),
    path('ver_clientes/', ver_clientes, name="ver_cli"),
]