from django.shortcuts import render
from app_super.models import *
from app_super.forms import *


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



def busqueda_proveedor(request):

    return render(request, "app_super/busqueda_proveedor.html")



def buscar_proveedor(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        nombres = Proveedor.objects.filter(nombre__icontains=nombre) # nombre=nombre
        return render(request, "app_super/buscar_proveedor.html", {"nombres":nombres})
    else:
        return render(request, "app_super/busqueda_proveedor.html", {"mensaje":"Ingrese un nombre."})


def ver_proveedores(request):
    lista_proveedores = Proveedor.objects.all()

    return render(request, "app_super/ver_proveedores.html", {"lista_proveedores" : lista_proveedores})



def empleado_form(request):
    if request.method == 'POST':
        mi_formulario = Empleado_form(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            empleado = Empleado(nombre = informacion['nombre'],
                                apellido = informacion['apellido'],
                                telefono = informacion['telefono'],
                                email = informacion['email'],
                                nacimiento = informacion['nacimiento'],
                                documento = informacion['documento'])
            empleado.save()
            return render(request, "app_super/inicio.html", {"mensaje":"Empleado creado exitosamente."})
    else:
        mi_formulario = Empleado_form()
    return render(request, "app_super/add_empleado.html", {"mi_formulario":mi_formulario})



def busqueda_empleado(request):

    return render(request, "app_super/busqueda_empleado.html")



def buscar_empleado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        nombres = Empleado.objects.filter(nombre__icontains=nombre)
        return render(request, "app_super/buscar_empleado.html", {"nombres":nombres})
    else:
        return render(request, "app_super/busqueda_empleado.html", {"mensaje":"Ingrese un nombre."})


def ver_empleados(request):
    lista_empleados = Empleado.objects.all()

    return render(request, "app_super/ver_empleados.html", {"lista_empleados" : lista_empleados})



def cliente_form(request):
    if request.method == 'POST':
        mi_formulario = Cliente_form(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente = Cliente(nombre = informacion['nombre'],
                              apellido = informacion['apellido'],
                              telefono = informacion['telefono'],
                              email = informacion['email'])
            cliente.save()
            return render(request, "app_super/inicio.html", {"mensaje":"Cliente creado exitosamente."})
    else:
        mi_formulario = Cliente_form()
    return render(request, "app_super/add_cliente.html", {"mi_formulario":mi_formulario})



def busqueda_cliente(request):

    return render(request, "app_super/busqueda_cliente.html")



def buscar_cliente(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        nombres = Cliente.objects.filter(nombre__icontains=nombre)
        return render(request, "app_super/buscar_cliente.html", {"nombres":nombres})
    else:
        return render(request, "app_super/busqueda_cliente.html", {"mensaje":"Ingrese un nombre."})


def ver_clientes(request):
    lista_clientes = Cliente.objects.all()

    return render(request, "app_super/ver_clientes.html", {"lista_clientes" : lista_clientes})