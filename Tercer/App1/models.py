from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre= models.CharField(max_length=40)
    codigodeventa= models.IntegerField()
class Vendedor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    tarjeta= models.CharField(max_length=30)
class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaentrega= models.DateField()
    entregado= models.BooleanField()