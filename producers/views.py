from producers.models import Producer
from rest_framework import generics
from producers.serializer import ProducerSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsActive

# Create your views here.


class ProducerCreateAPIView(generics.CreateAPIView):
    """ APIView for creating Producer """
    serializer_class = ProducerSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProducerListAPIView(generics.ListAPIView):
    """ APIView for send list of Producers """
    serializer_class = ProducerSerializer
    permission_classes = [IsAuthenticated, IsActive]
    queryset = Producer.objects.all()


class ProducerUpdateAPIView(generics.UpdateAPIView):
    """ APIView for updating Producer """
    serializer_class = ProducerSerializer
    permission_classes = [IsAuthenticated, IsActive]
    queryset = Producer.objects.all()

    def perform_update(self, serializer):
        pass


class ProducerDestroyAPIView(generics.DestroyAPIView):
    """ APIView for deleting Producer """
    serializer_class = ProducerSerializer
    permission_classes = [IsAuthenticated, IsActive]
    queryset = Producer.objects.all()


class ProducerRetrieveAPIView(generics.RetrieveAPIView):
    """ APIView for sending information about Producer """
    serializer_class = ProducerSerializer
    permission_classes = [IsAuthenticated, IsActive]
    queryset = Producer.objects.all()
