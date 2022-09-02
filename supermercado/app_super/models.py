from django.db import models

# Create your models here.


class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=50)
    nombre_viajante = models.CharField(max_length=50)
    telefono_empresa = models.IntegerField()
    telefono_viajante = models.IntegerField()
    email_empresa = models.EmailField()
    email_viajante = models.EmailField()


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email = models.EmailField()
    nacimiento = models.DateField()
    documento = models.IntegerField()


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email = models.EmailField()