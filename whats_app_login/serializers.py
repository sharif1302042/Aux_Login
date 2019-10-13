from rest_framework import serializers

from .models import LoginCredential


class LoginCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginCredential
        fields = ('browser_name', 'browser_version', 'device_ip',)
