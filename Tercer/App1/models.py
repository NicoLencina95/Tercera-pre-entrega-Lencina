from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre= models.CharField(max_length=40)
    codigodeventa= models.IntegerField()
    def __str__(self):
            return f"Producto: {self.nombre} - Código de venta {self.codigodeventa}"
class Vendedor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
            return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email}"
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    tarjeta= models.CharField(max_length=30)
    def __str__(self):
            return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Tarjeta {self.tarjeta}"
class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaentrega= models.DateField()
    entregado= models.BooleanField()
    def __str__(self):
            return f"Nombre: {self.nombre} - Fecha de entrega {self.fechaentrega} - Entragado? {self.entregado}"