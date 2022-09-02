from django import forms

class Proveedor_form(forms.Form):
    nombre = forms.CharField(max_length=50)
    telefono = forms.IntegerField()
    email = forms.EmailField()