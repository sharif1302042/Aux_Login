import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import LoginCredential, EventIdentifier
from .serializers import LoginCredentialSerializer, LoginSerializer
from applibs.circle_backends import circle_backends
from applibs.qr_code_generators import qr_code_generator


class QrCodeGenerator(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'qr_code.html'

    def get(self, request):

        try:
            identifier = EventIdentifier.objects.create_unique_identifier()
            print("idntifier",identifier)
            credentials = {
                #"device_name": request.user_agent.device,
                "browser_name": request.user_agent.browser.family,
                "browser_version": request.user_agent.browser.version_string,
                "user_ip": request.META.get('REMOTE_ADDR'),
                "identifier": str(identifier)
            }
            qr_code = qr_code_generator.qr_code_with_pyqrcode(credentials)
            print(qr_code)
            return Response({"credentials": credentials}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error_code": "errors"}, status=status.HTTP_200_OK)


class LoginCredentialFromAPP(APIView):
    def post(self, request):
        try:
            serilizer = LoginSerializer(data=request.data, )  # valided requested data via serializer
            if serilizer.is_valid():
                if LoginCredential.objects.verify_user(serilizer.data,
                                                       request.user.username):  # varify the requested user credentials

                    #This Section is for comunicating from views to consumer that is
                    #when user is successfully logged in.
                    channel_layer = get_channel_layer()
                    print(channel_layer)
                    msg = "event Trigered with identifier {}".format(request.data['identifier'])
                    async_to_sync(channel_layer.group_send)(
                        request.data['identifier'],
                        {
                            'type': 'send_message_to_frontend',
                            'message': msg
                        }
                    )
                    return Response({"credentials": serilizer.data, "user_name": request.user.username},
                                    status=status.HTTP_200_OK)
            return Response({'error_code': serilizer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'error_code': str(e)}, status=status.HTTP_400_BAD_REQUEST)


#####################################for websocket#########################
def event_triger(request):
    channel_layer = get_channel_layer()
    print(channel_layer)
    async_to_sync(channel_layer.group_send)(
        'event_sharif',
        {
            'type': 'send_message_to_frontend',
            'message': "event_trigered_from_views"
        }
    )
    return HttpResponse('<p>Done</p>')


class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'otp.html'

    def get(self, request):
        return Response({"room": "room"}, status=status.HTTP_200_OK)


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
