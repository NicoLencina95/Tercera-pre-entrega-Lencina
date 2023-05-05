
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
    path('leerVendedores',views.leerVendedores,name='LeerVendedores'),
    path('eliminarVendedor/<vendedor_nombre>/', views.eliminarVendedor, name="EliminarVendedor"),
    path('editarVendedor/<vendedor_nombre>/', views.editarVendedor, name="EditarVendedor"),
    path('productos/', views.productos, name='productos'),
    path('busquedaProducto', views.busqueda_producto, name='busquedaProducto'),
    path('producto/list',views.ProductoList.as_view(),name='List'),
    path(r'^(?P<pk>/d+)$', views.ProductoDetalle.as_view(),name='Detail'),
    path(r'^nuevo$', views.ProductoCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>/d+)$',views.ProductoUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>/d+)$',views.ProductoDelete.as_view(),name='Delete'),

    path('listaProducto',views.ProductoList.as_view(), name='listaProducto'),
    

   
]