from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        
        return f" Nombre:  {self.nombre} - Telefono:  {self.telefono} - email:  {self.email}"




class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    nacimiento = models.DateField()
    documento = models.IntegerField()
    
    def __str__(self):
        
        return f" Nombre: {self.nombre} - Apellido:  {self.apellido} -Telefono:  {self.telefono} - email:  {self.email} - Nacimiento:  { self.nacimiento} - Documento:  {self.documento}"




class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        
        return f" Nombre:  {self.nombre} - Apellido:  {self.apellido} -Telefono:  {self.telefono} - email:  {self.email}"