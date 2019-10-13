from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.contrib.auth import get_user_model

from applibs.circle_backends import circle_backends

User = get_user_model()


class LoginCredentialManager(models.Manager):
    def verify_user(self, requested_data, user):
        if circle_backends.is_user_connect_id_exists(user):
            login_credentials = self.filter(user__username=user)[0]
            if not login_credentials:
                raise Exception("No Info Found")

            if not login_credentials.device_ip == requested_data['device_ip']:  # check device_ip
                raise Exception("Device IP Not Match")

            if not login_credentials.browser_name == requested_data['browser_name']:  # check browser
                raise Exception("Browser Not Match")

            if not login_credentials.browser_version == requested_data['browser_version']:  # check browser version
                raise Exception("Browser Version Not Match")
            return True
        raise Exception("invalid Connect ID")


class LoginCredential(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    browser_name = models.CharField(max_length=50)
    browser_version = models.CharField(max_length=30)
    device_ip = models.CharField(max_length=50)
    device_uid = models.UUIDField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LoginCredentialManager()

    def __str__(self):
        return "{}-{}-{}".format(self.user, self.browser_name, self.browser_version)

    class Meta:
        verbose_name = 'User Login Credential'
        verbose_name_plural = 'User Login Credentials'

        """use Postgre SQL database to use BrinIndex"""
        indexes = (
            BrinIndex(fields=["id", "created_at", "updated_at"]),
        )
