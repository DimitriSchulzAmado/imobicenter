from django.db import models


class PropertyType(models.TextChoices):
    RESIDENCIAL = "Residencial", "Residencial"
    COMERCIAL = "Comercial", "Comercial"


class Property(models.Model):
    address = models.CharField(max_length=300)
    cep = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=PropertyType.choices)
    iptu_inscription = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.address)
