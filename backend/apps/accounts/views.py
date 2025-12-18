from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(["POST"])
@permission_classes([AllowAny])
def signup_view(request):
    form = UserCreationForm(request.data)

    if form.is_valid():
        user = form.save()
        return JsonResponse(
            {
                "user": {
                    "id": user.id,
                    "username": user.username,
                }
            },
            status=status.HTTP_201_CREATED,
        )

    return JsonResponse({"errors": form.errors}, status=status.HTTP_400_BAD_REQUEST)
