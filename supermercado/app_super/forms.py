from django import forms

class Proveedor_form(forms.Form):
    nombre = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.EmailField()


class Empleado_form(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.EmailField()
    nacimiento = forms.DateField()
    documento = forms.IntegerField()


class Cliente_form(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.EmailField()