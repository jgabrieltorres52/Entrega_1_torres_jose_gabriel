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
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            # cleaned data devuelve un diccionario {'nombre':'abc', 'telefono':123, 'email':abc@xyz}
            proveedor = Proveedor(nombre = informacion['nombre'],
                                  telefono = informacion['telefono'],
                                  email = informacion['email'])
            proveedor.save()
            return render(request, "app_super/inicio.html", {"mensaje":"Proveedor creado exitosamente."})
    else:
        mi_formulario = Proveedor_form()
    return render(request, "app_super/add_proveedor.html", {"mi_formulario":mi_formulario})



def buscar_proveedor(request):

    return render(request, "app_super/buscar_proveedor.html")



def buscar_prov(request):
    nombre = request.GET["nombre"]
    respuesta = f"estoy buscando al proveedor {nombre}"
    return HttpResponse(respuesta)



def ver_proveedores(request):

    pass


def empleado_form(request):

    pass



def buscar_empleado(request):

    pass



def buscar_emp(request):

    pass



def ver_empleados(request):

    pass



def cliente_form(request):

    pass



def buscar_cliente(request):

    pass



def buscar_cli(request):

    pass



def ver_clientes(request):

    pass