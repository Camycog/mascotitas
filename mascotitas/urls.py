from unicodedata import name
from django.urls import path, include
from .views import home,contacto,agregar_producto


urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto")
    path('agregar-producto/', agregar_producto, name="agregar_producto")
]