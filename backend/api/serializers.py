from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        # we accept a new user and return a new user. (serializer is used in two differents places)
        extra_kwargs = {"password": {"write_only": True}}
        # We want to accept password when we creating a new user
        # We don't want to return password when we givin information of this user

        def create(self, validated_data):
            print(validated_data)
            user = User.objects.create_user(**validated_data)
            return user
