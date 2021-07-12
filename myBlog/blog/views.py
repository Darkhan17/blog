from django.shortcuts import render
from rest_framework.views import APIView

from API.serializers import BlogSerializer,AuthorSerializer,ProjectSerializer
from rest_framework.response import Response

from rest_framework import permissions
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response