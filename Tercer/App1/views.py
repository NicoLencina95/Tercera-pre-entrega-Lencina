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
    return render(request, 'App1/inicio.html')
def productos(request):
    return render(request,'App1/productos.html')
def vendedores(request):
    return render(request,'App1/vendedores.html')
def clientes(request):
    return render(request,'App1/clientes.html')
def entregables(request):
    return render(request,'App1/entregables.html')



from App1.forms import ProductoFormulario,VendedorFormulario
from App1.models import Vendedor


def productos(request):
    if request.method =='POST':
        miFormulario=ProductoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            producto=Producto(int(informacion['id']),str(informacion['nombre']),int(informacion['codigodeventa']))
            producto.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=ProductoFormulario()
    return render(request, 'App1/productos.html', {"miFormulario": miFormulario})


def vendedorFormulario(request):
     if request.method == "POST":
        miFormulario = VendedorFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            vendedor = Vendedor(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['email'])
            vendedor.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = VendedorFormulario()
             
     return render(request, "App1/vendedorFormulario.html", {"miFormulario": miFormulario})


from App1.models import Cliente
from App1.forms import ClienteFormulario
def clienteFormulario(request):
     if request.method == "POST":
        miFormulario = ClienteFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Cliente(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['email'], informacion['tarjeta'])
            cliente.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = ClienteFormulario()
             
     return render(request, "App1/clienteFormulario.html", {"miFormulario": miFormulario})

from App1.models import Entregable
from App1.forms import EntregableFormulario
def entregableFormulario(request):
     if request.method == "POST":
        miFormulario = EntregableFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            entregable = Entregable(int(informacion['id']),str(informacion['nombre']),informacion['fechaentrega'],
                                   bool(informacion['entregado']))
            entregable.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = EntregableFormulario()
             
     return render(request, "App1/entregableFormulario.html", {"miFormulario": miFormulario})

def busquedaProducto(request):
     return render(request,'App1/busquedaProducto.html')

def buscar(request):
     if request.GET['producto']:
          producto = request.GET['producto']
          productos = Producto.objects.filter(codigodeventa__icontains=producto)

          return render(request,'App1/resultadosBusqueda.html', {"productos":productos, "producto_buscado": producto})
     else:
          respuesta= "No enviaste datos"

     return HttpResponse(respuesta)

def leerVendedores(request):
    vendedores= Vendedor.objects.all() # trae a todos los pendedores
    contexto= {"vendedores": vendedores}
    return render(request, "App1/leerVendedores.html",contexto)

def eliminarVendedor(request, vendedor_nombre):
    vendedor = Vendedor.objects.get(nombre=vendedor_nombre)
    vendedor.delete()
    # vuelvo al menú
    vendedores = Vendedor.objects.all()  # trae todos los pendedores 
    contexto = {"vendedores": vendedores}
    return render(request, "App1/leerVendedores.html", contexto)

def editarVendedor(request, vendedor_nombre):
    # Recibe el nombre del pendedor que vamos a modificar
    vendedor = Vendedor.objects.get(nombre=vendedor_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = VendedorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            vendedor.nombre = informacion['nombre']
            vendedor.apellido = informacion['apellido']
            vendedor.email = informacion['email']
            
            vendedor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "App1/inicio.html")
   # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = VendedorFormulario(initial={'nombre': vendedor.nombre, 'apellido': vendedor.apellido,
                                                   'email': vendedor.email})
    # Voy al html que me permite editar
    return render(request, "App1/editarVendedor.html", {"miFormulario": miFormulario, "vendedor_nombre": vendedor_nombre})                 

from django.shortcuts import render

def busqueda_producto(request):
    return render(request, 'busquedaProducto.html')

from django.views.generic import ListView
class ProductoList(ListView):
    model =Producto 
    template_name='/App1/producto_list.html'

from django.views.generic.detail import DetailView
class ProductoDetalle(DetailView):
    model=Producto 
    template_name= "App1/producto_detalle.html"

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
class ProductoCreacion(CreateView):
    model=Producto
    success_url="/App1/producto/list"
    fields= ['nombre','codigodeventa']

from django.views.generic.edit import UpdateView
class ProductoUpdate(UpdateView):
    model=Producto
    success_url= "/App1/producto/list"
    fields=['nombre','codigodeventa']

from django.views.generic.edit import DeleteView
class ProductoDelete(DeleteView):
    model=Producto
    success_url="/App1/producto/list"


def lista_producto(request):
    return render(request, 'producto_list.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto_list.html', {'productos': productos})