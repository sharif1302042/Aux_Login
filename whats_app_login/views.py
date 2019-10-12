from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import LoginCredential
from .serializers import LoginCredentialSerializer
from applibs.circle_backends import circle_backends
from applibs.qr_code_generators import qr_code_generator


class QrCodeGenerator(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'qr_code.html'

    def get(self, request):

        try:
            credentials = {
                "device_name": request.user_agent.device,
                "browser_name": request.user_agent.browser.family,
                "browser_version": request.user_agent.browser.version_string,
                "user_ip": request.META.get('REMOTE_ADDR'),
                "user_name": "sharif_42"
            }
            qr_code = qr_code_generator.qr_code_with_pyqrcode(credentials)
            print(qr_code)
            return Response({"credentials": credentials}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error_code": "errors"}, status=status.HTTP_200_OK)


class LoginCredentialView(APIView):

    def post(self, request):
        serilizer = LoginCredentialSerializer(data=request.data)
        if serilizer.is_valid():
            if circle_backends.is_user_connect_id_exists('01780510000'):
                pass
            return Response({'error_code': "Invalid Connect ID"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error_code': "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)
