from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.Consumer),
    re_path(r'ws/otp_browser_auth/$', consumers.Consumer),
    re_path(r'ws/otp_for_device/$', consumers.Consumer),
]