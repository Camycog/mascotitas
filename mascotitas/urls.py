from django.urls import path
from .views import home,contacto


urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto")
]