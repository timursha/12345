from rest_framework import viewsets, permissions

from map.models import Shop, Product
from map.serializers import ShopSerializer, ProductSerializer


class ShopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

