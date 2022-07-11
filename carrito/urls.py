
from django.urls import path, include
from . import views

app_name="carrito"

urlpatterns = [
    path("agregar/<int:producto_id/", views.agregar_carrito, name="agregar"),
    path("eliminar/<int:producto_id/", views.eliminar_carrito, name="eliminar"),
    path("restar/<int:producto_id/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_carrito, name="limpiar"),
]