

# Create your views here.
from django.shortcuts import render
from App1.models import Producto
from django.http import HttpResponse

def producto(self):
    producto = Producto(nombre="Coquita",codigodeventa=19673)
    producto.save()
    texto= f"----> producto: {producto.nombre}, codigodeventa: {producto.codigodeventa}"
    return HttpResponse(texto)

    