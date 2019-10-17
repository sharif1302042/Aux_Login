from rest_framework import serializers

from .models import LoginCredential


class LoginCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginCredential
        fields = ('browser_name', 'browser_version', 'device_ip',)

class LoginSerializer(serializers.Serializer):
    browser_name = serializers.CharField(max_length=50)
    browser_version = serializers.CharField(max_length=50)
    device_ip = serializers.CharField(max_length=50)
    identifier = serializers.CharField(max_length=200)
