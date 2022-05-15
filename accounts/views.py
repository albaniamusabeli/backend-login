from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

### COPIADO DESDE DJANGO REST FRAMEWORK https://www.django-rest-framework.org/api-guide/authentication/

class ProfileView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            ##'user': str(request.user),  # `django.contrib.auth.User` instance.
            'user': str(request.user.correo),
            'auth': str(request.auth),  # None
        }
        return Response(content)