from dataclasses import fields
from .models import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    nombre_marca = serializers.CharField(read_only=True, source="marca.nombre")
    class Meta:
        model = Producto
        fields = '__all__'

        
    