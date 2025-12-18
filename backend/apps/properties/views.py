from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from .models import Property
from .serializers import PropertySerializer


class PropertyList(ListAPIView):
    queryset = Property.objects.order_by("-created_at")
    context_object_name = "properties"
    serializer_class = PropertySerializer


class PropertyDetail(RetrieveAPIView):
    context_object_name = "property"
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyRegister(CreateAPIView):
    serializer_class = PropertySerializer

    def perform_create(self, serializer):
        serializer.save()


class PropertyUpdate(UpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    context_object_name = "property"

    def perform_update(self, serializer):
        serializer.save()


class PropertyDelete(DestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    context_object_name = "property"

    def perform_destroy(self, instance):
        instance.delete()
