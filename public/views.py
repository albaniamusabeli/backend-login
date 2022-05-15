from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

### COPIADO DESDE DJANGO REST FRAMEWORK https://www.django-rest-framework.org/api-guide/authentication/

class IndexView(APIView):

    def get(self, request, format=None):
        content = {
            'wmsg': 'Hola desde el Backend de Django (app public)'
        }
        return Response(content)