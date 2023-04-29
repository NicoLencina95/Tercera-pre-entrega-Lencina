

# Create your views here.
from django.shortcuts import render
from App1.models import Producto
from django.http import HttpResponse

def producto(self):
    producto = Producto(nombre="Coquita",codigodeventa=19673)
    producto.save()
    texto= f"----> producto: {producto.nombre}, codigodeventa: {producto.codigodeventa}"
    return HttpResponse(texto)

    from django.shortcuts import render


# Create your views here.
def inicio(request):
    return HttpResponse("vista inicio")
def productos(request):
    return HttpResponse('vista productos')
def vendedores(request):
    return HttpResponse('vista vendedores')
def clientes(request):
    return HttpResponse('vista clientes') 
def entregables(request):
    return HttpResponse('vista entregables')

from django.shortcuts import render
from App1.models import Producto
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def productos(request):
    return render(request,'App1/productos.html')
def vendedores(request):
    return render(request,'App1/vendedores.html')
def clientes(request):
    return render(request,'App1/clientes.html')
def entregables(request):
    return render(request,'App1/entregables.html')