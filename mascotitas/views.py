from itertools import product
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ContactoForm, CustomUserCreationForm, ProductoForm
from django.contrib import messages
from django.http import Http404
from django.contrib.auth import authenticate,login

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
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'mascotitas/producto/agregar.html', data)

def listar_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'mascotitas/producto/listar.html', data)

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id)
        data = {
            'form': ProductoForm(instance=producto)
        }
        if request.method == 'POST':
            formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Modificado correctamente")
                return redirect(to="listar_productos")
            data["form"] = formulario
    return render(request, 'mascotitas/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_productos")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data("username"),password=formulario.cleaned_data("password1"))
            login(request, user)
            return redirect(to="home")
        data["form" ]= formulario   
    return render(request, 'mascotitas/registration/registro.html', data)

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'mascotitas/productos.html', data)
