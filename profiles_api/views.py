from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format = None):
        """Returns list of API view features"""
        an_apiview = [
            'Uses http methods as functions - get, post, put, patch, delete',
            'Similar to traditional Django View',
            'Gives maximum control over application logic',
            'Mapped manually to URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    