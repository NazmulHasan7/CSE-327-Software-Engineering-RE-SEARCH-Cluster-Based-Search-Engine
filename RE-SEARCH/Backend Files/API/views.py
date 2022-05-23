from re import I
import requests
from django.shortcuts import render
from .serializers import cluster_serializer, url_serializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from base_app.models import Cluster, Url


from django.http import HttpResponse
from django.http import JsonResponse

from .serializers import RegisterSerializer

from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView)





from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication


from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import (
	AllowAny,
	)


# Create your views here.


    #Api Views for all the models

class ClusterAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        user=self.request.user
        queryset = Cluster.objects.filter(user=user)
        serializer = cluster_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =cluster_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class URL_API(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        queryset = Url.objects.all()
        serializer = url_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =url_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   


#User API view containing all the userinfo for future reference

'''
class UserAPI(APIView):

    def get(self, requests, format=None):
        """ print(uname)
        u = User.objects.filter(username=uname)
        serializer = user_serializer(u, many=True)
        return Response(serializer.data)
        """
        
        """ user = self.request.user
        queryset = User.objects.filter(user=user) """

        queryset = User.objects.all()
        serializer = user_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =user_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    

    def User(self):
        pass
'''

""" user_list = ClusterAPI.as_view({'get': 'list'})
user_detail = ClusterAPI.as_view({'get': 'retrieve'})
print(user_list)
for i in user_list:
    print(i)

print("Success") """


class Register(CreateAPIView):
	permission_classes = (AllowAny,)

	serializer_class = RegisterSerializer
	queryset = User.objects.all()