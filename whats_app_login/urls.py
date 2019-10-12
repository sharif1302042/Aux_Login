from django.urls import path
from whats_app_login import views

urlpatterns = [
    path('get_qr_code/', views.QrCodeGenerator.as_view(), name='qr_code'),
]
