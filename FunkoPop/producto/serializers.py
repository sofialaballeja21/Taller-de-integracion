from rest_framework import serializers

from producto.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        # fields = ['name', 'number', 'collection', 'edition', 'price', 'is_backlight']
        fields = '__all__'