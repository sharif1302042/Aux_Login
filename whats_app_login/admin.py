from django.contrib import admin

from .models import LoginCredential, EventIdentifier


class LoginCredentialAdmin(admin.ModelAdmin):
    search_fields = ('pk',)
    list_display = ('pk', 'user', 'browser_name', 'browser_version', 'device_ip')


class EventIdentifierAdmin(admin.ModelAdmin):
    list_display = ('pk', 'identifier')


admin.site.register(LoginCredential, LoginCredentialAdmin)
admin.site.register(EventIdentifier, EventIdentifierAdmin)
