from products.models import Product
from rest_framework import generics
from products.serializer import ProductSerializer

# Create your views here.


class ProductCreateAPIView(generics.CreateAPIView):
    """ APIView for creating Product """
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    """ APIView for send list of products """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(generics.UpdateAPIView):
    """ APIView for updating product """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(generics.DestroyAPIView):
    """ APIView for deleting product """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """ APIView for sending information about product """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
