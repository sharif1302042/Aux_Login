from django.urls import path
from whats_app_login import views

urlpatterns = [
    path('get_qr_code/', views.QrCodeGenerator.as_view(), name='qr_code'),
    path('login_credentials_from_app/', views.LoginCredentialFromAPP.as_view(), name='login_credentials'),

    ###################for web socket################################
    path('home/', views.Home.as_view(), name='home'),
    path('otp/<str:room_name>/', views.room, name='room'),

    path('event/',views.alarm,name='event')
]
