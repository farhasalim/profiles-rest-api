from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from profiles_api import serializers

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Returns list of API view features"""
        an_apiview = [
            'Uses http methods as functions - get, post, put, patch, delete',
            'Similar to traditional Django View',
            'Gives maximum control over application logic',
            'Mapped manually to URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Person knows what went wrong if he submits an invalid request
        
    def put(self, request, pk = None):
        """Handle updation of an object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk = None):
        """Handle partial updation of an object - i.e. only fields specified in the request"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk = None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
    