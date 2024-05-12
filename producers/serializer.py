from rest_framework import serializers
from producers.models import Producer


class ProducerSerializer(serializers.ModelSerializer):
    """Serializer for User Model"""
    class Meta:
        model = Producer
        fields = "__all__"
        search_fields = ['country']
        read_only_fields = ['debt']
        extra_kwargs = {
            'debt': {'write_only': True}
        }
