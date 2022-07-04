from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pacientes(models.Model): 
    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()
    dni= models.IntegerField()
    telefono= models.IntegerField('', default=0)
    email= models.EmailField('', default="No informado")
    #patologia= models.CharField(max_length=40) # ver #
    #talla= models.IntegerField()
    #peso= models.IntegerField()
    #contorno= models.IntegerField() # se espera que ingrese contorno cintura #

    #agregado CLASE 22 para mejorar la vista de administrador#
    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad} - DNI: {self.dni} - Teléfono: {self.telefono} - Email: {self.email}"


class Prestadores(models.Model):
    nombre= models.CharField(max_length=40)
    especialidad= models.CharField(max_length=40)
    telefono= models.IntegerField('', default=0)
    email= models.EmailField('', default="No informado")

    #agregado CLASE 22 para mejorar la vista de administrador#
    def __str__(self):
        return f"Nombre: {self.nombre} - Especialidad: {self.especialidad} - Teléfono: {self.telefono} - Email: {self.email}"


class Proveedores(models.Model):
    nombre= models.CharField(max_length=40)
    cuit= models.IntegerField()
    cbu= models.IntegerField()
    telefono= models.IntegerField('', default=0)
    email= models.EmailField('', default="No informado")

    #agregado CLASE 22 para mejorar la vista de administrador#
    def __str__(self):
        return f"Nombre: {self.nombre} - CUIT: {self.cuit} - CBU: {self.cbu} - Teléfono: {self.telefono} - Email: {self.email}"

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)