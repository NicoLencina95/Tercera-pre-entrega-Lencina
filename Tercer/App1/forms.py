from django import forms
 
class ProductoFormulario(forms.Form):
    id= forms.IntegerField()
    nombre = forms.CharField()
    codigodeventa = forms.IntegerField()
class VendedorFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
class ClienteFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    tarjeta= forms.CharField(max_length=30)
class EntregableFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    fechaentrega= forms.DateField()
    entregado= forms.BooleanField()