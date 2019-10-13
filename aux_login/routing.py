from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.conf.urls import url

import whats_app_login.routing
from whats_app_login.consumers import OTPConsumer
# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             whats_app_login.routing.websocket_urlpatterns
#         )
#     ),
# })

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            url(r"^api/v1/home$",OTPConsumer),
        )
    )

})