from rest_framework import serializers
from .models import CustomUser, UserProfile, AddressGlobal


class AddressGlobalSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddressGlobal
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    address_info = AddressGlobalSerializer()

    class Meta:
        model = UserProfile
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ("email", "name", "user_profile", "created_at", "updated_at")
