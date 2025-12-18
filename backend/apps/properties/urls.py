from django.urls import path

from .views import (
    PropertyDelete,
    PropertyDetail,
    PropertyList,
    PropertyRegister,
    PropertyUpdate,
)

urlpatterns = [
    path("", PropertyList.as_view(), name="property-list"),
    path("<int:pk>/", PropertyDetail.as_view(), name="property-detail"),
    path("register/", PropertyRegister.as_view(), name="property-register"),
    path("update/<int:pk>", PropertyUpdate.as_view(), name="property-update"),
    path("delete/<int:pk>", PropertyDelete.as_view(), name="property-delete"),
]
