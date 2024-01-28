"""
Basic home view
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from home.serializers import UserSerializer

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    Registration view
    """
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    # Validate data
    if not username or not password or not email:
        return Response({'error': 'All fields must be provided'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username is already taken'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, email=email)

    # Log the user in
    login(request, user)

    return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)



@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    """
    Login view
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Both username and password must be provided'}, status=status.HTTP_400_BAD_REQUEST)

    # Authenticate the user
    user = authenticate(request, username=username, password=password)

    # Check if authentication is successful
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_users(request):
    """
    View to retrieve and display all user data.
    """
    # Retrieve all user data
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response({'users': serializer.data}, status=status.HTTP_200_OK)