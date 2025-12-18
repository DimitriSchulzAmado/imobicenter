from django.contrib import admin

from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "address",
        "cep",
        "type",
        "iptu_inscription",
        "created_at",
        "updated_at",
    )
    search_fields = ("address", "cep", "iptu_inscription")
    list_filter = ("type", "created_at", "updated_at")
    ordering = ("-created_at",)


admin.site.register(Property)
