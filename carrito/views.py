from django.shortcuts import render, redirect
from .carrito import Carrito
from mascotitas.models import Producto



# Create your views here.

def agregar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar_carrito(producto = producto)
    return redirect("productos")

def eliminar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar_carrito(producto = producto)
    return redirect("productos")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar_producto(producto = producto)
    return redirect("productos")

def limpiar_carrito(request, producto_id):
    carrito = Carrito(request)
    carrito.limpiar_carrito()
    return redirect("productos")

