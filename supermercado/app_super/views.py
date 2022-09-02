from django.shortcuts import render
from django.http import HttpResponse
from app_super.models import *
from app_super.forms import *

# Create your views here.

def inicio(request):

    return render(request, "app_super/inicio.html")

def proveedor_form(request):
    if request.method == 'POST':
        mi_formulario = Proveedor_form(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            proveedor = Proveedor(nombre = informacion['nombre'],
                                  telefono = informacion['telefono'],
                                  email = informacion['email'])
            proveedor.save()
            return render(request, "")
    else:
        mi_formulario = Proveedor_form()
    return render(request, "app_super/add_proveedor.html", {"mi_formulario":mi_formulario})



def buscar_proveedor(request):

    pass



def ver_proveedores(request):

    pass


def empleado_form(request):

    pass



def buscar_empleado(request):

    pass



def ver_empleados(request):

    pass



def cliente_form(request):

    pass



def buscar_cliente(request):

    pass



def ver_clientes(request):

    pass