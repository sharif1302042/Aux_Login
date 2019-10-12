from django.shortcuts import render

# from .models import LoginCredential
#
# class VerifyLoginCredentials(APIView):
#     def get(self,request):
#         credentials = {
#             "device_name":request.user_agent.device,
#             "browser_name":request.user_agent.browser.family,
#             "browser_version":request.user_agent.browser.version_string,
#             "user_ip":request.META.get('REMOTE_ADDR')
#         }
#         return Response({"credentials":credentials}, status = status.HTTP_200_OK)
