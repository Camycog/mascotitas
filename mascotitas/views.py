from django.shortcuts import render
from .models import Producto
from .forms import Contacto



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
    return render(request, 'mascotitas/contacto.html', data)