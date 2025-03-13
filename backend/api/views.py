from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import UserSerializer


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    # Verify every objects for indefy that we can create a unique User
    serializer_class = UserSerializer
    # Tells this view what kind of data we need to accept to make new User
    permission_classes = [AllowAny]
    # Who can actually call this
