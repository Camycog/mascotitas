
from django.urls import path, include
from . import views

app_name= "carrito"
urlpatterns = [
    path("agregar_carrito/<int:producto_id>/", views.agregar_carrito, name="agregar"),
    path("eliminar_carrito/<int:producto_id>/", views.eliminar_carrito, name="eliminar"),
    path("restar_producto/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar_carrito/", views.limpiar_carrito, name="limpiar"),
]