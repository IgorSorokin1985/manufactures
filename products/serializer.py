from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for User Model"""
    class Meta:
        model = Product
        fields = "__all__"
