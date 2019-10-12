from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginCredentialManager(models.Manager):
    pass


class LoginCredential(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user',null=True,blank=True)
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
