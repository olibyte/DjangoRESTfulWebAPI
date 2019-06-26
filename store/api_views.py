from rest_framework.generics import ListAPIView

from store.serializers import ProductSerializer
from store.models import Product

class ProductList(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer