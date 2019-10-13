from django.contrib import admin

from .models import LoginCredential,Client

class LoginCredentialAdmin(admin.ModelAdmin):
    search_fields = ('pk',)
    list_display = ('pk','user','browser_name','browser_version','device_ip')

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('pk','channel_name')

admin.site.register(LoginCredential,LoginCredentialAdmin)
admin.site.register(Client,ClientsAdmin)