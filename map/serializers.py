from map.models import Shop, Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'compound', 'price', 'photo', 'energy', 'weight', 'category')


class ShopSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = ('id', 'latitude', 'longitude', 'products')
