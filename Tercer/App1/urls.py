
from django.urls import path
from App1 import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('productos', views.productos, name="Productos"),
    path('vendedores', views.vendedores, name="Vendedores"),
    path('clientes', views.clientes, name="Clientes"),
    path('entregables', views.entregables, name="Entregables"),
    #path('productoFormulario', views.productoFormulario, name="ProductoFormulario"),
    path('vendedorFormulario', views.vendedorFormulario, name="VendedorFormulario"),
    path('clienteFormulario', views.clienteFormulario, name="ClienteFormulario"),
    path('entregableFormulario', views.entregableFormulario, name="EntregableFormulario"),
    path('busquedaProducto',views.busquedaProducto,name="BusquedaProducto"),
    path('buscar/',views.buscar),
]