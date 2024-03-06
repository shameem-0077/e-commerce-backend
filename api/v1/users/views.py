from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.v1.users.serializers import *
from users.models import Customer


@api_view(['POST'])
@permission_classes((AllowAny,))
def sign_up(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data['username']
        first_name = serializer.data['first_name']
        last_name = serializer.data['last_name']
        email = serializer.data['email']
        phone = serializer.data['phone']
        password = serializer.data['password']

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        Customer.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email
        )

        response_data = {
            "status_code": 6000,
            "title": "success",
            "message": "user created"
        }
    
    else:
        response_data = {
            "status_code": 6001,
            "title": "failed",
            "message": serializer._errors
        }

    return Response(response_data, status=status.HTTP_200_OK)