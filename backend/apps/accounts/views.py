import json

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            # login(request, user) # Log the user in automatically after signup
            # return redirect('home') # Redirect to the home view
            return JsonResponse({'form': form})
    else:
        form = UserCreationForm()
    # return render(request, 'registration/signup.html', {'form': form})
    return form

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Aqui você pode usar JWT ou Token do DRF
            return JsonResponse({
                'token': 'seu_token_aqui',
                'user': {
                    'id': user.id,
                    'email': user.email,
                }
            })
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
