from django.urls import path 
from App1 import views 

urlpatterns=[

    path('', views.inicio),
    path('productos', views.productos, name='Productos'),
    path('vendedores', views.vendedores),
    path('clientes', views.clientes),
    path('entregables', views.entregables),
]