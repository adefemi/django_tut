from rest_framework import serializers
from .models import CustomUser, UserProfile


class CustomeUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("email", "name", "created_at", "updated_at")


class UserProfileSerializer(serializers.ModelSerializer):
    user = CustomeUserSerializer()

    class Meta:
        model = UserProfile
        fields = "__all__"
