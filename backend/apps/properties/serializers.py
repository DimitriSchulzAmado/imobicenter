from rest_framework import serializers

from .models import Property


# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ["id", "address", "cep", "type", "iptu_inscription", "created_at"]
