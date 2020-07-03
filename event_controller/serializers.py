from rest_framework import serializers
from .models import EventMain, EventFeature
from user.serializers import AddressGlobalSerializer, CustomUserSerializer


class EventFeatureSerializer(serializers.ModelSerializer):
    eventmain = serializers.CharField(read_only=True)
    eventmain_id = serializers.Integer(write_only=True)

    class Meta:
        model = EventFeature
        fields = "__all__"


class EventMainSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    author_id = serializers.Integer(write_only=True)
    address_info = AddressGlobalSerializer(read_only=True)
    address_info_id = serializers.Integer(write_only=True)
    event_features = EventFeatureSerializer(read_only=True)

    class Meta:
        model = EventMain
        fields = "__all__"
