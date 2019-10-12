from django.contrib import admin

from .models import LoginCredential

class LoginCredentialAdmin(admin.ModelAdmin):
    search_fields = ('pk',)
    list_display = ('pk','user','browser_name','browser_version','device_ip')

admin.site.register(LoginCredential,LoginCredentialAdmin)