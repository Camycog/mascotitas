from django.shortcuts import render
from django.http import Http404
from .models import Producto
from .forms import ContactoForm



# Create your views here.
def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'mascotitas/home.html', data)

def contacto(request):
    data= {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'mascotitas/contacto.html', data)

def agregar_producto(request):
    return render(request, 'mascotitas/producto/agregar.html')