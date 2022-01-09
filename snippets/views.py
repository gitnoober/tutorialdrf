from collections import UserString
import re
from django.contrib.auth.models import User
from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers



from .serializers import SnippetSerializer,UserSerializer
from .models import Snippet
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse , HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
# Create your views here.


# class SnippetList(APIView):
#     """
#     List all code snippets, or create a new snippet.
#     """

#     def get(self, request , format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets , many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status = status.HTTP_201_CREATED)
#         return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST) # make reponse meaning more obvious

"""
Transforming the class based view above to another class based view using mixins and generics
explicitly binding "self.list/self.create" to their respective methods
"""
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]





# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk = pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request , pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet , data=request.data) # parse the request to json and serialize it
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

#     def delete(self , request,pk,format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return HttpResponse(status= status.HTTP_204_NO_CONTENT)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# adding generic api view to provide core functionality and adding in mixins for ops such as create, update , destroy

        
# request.data can handle other content data types, earlier I was just tying data to JSON
# now request.data handles everything
# returning Response objects, allowing REST framework to render the response into the correct content type for us.


class ListUser(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

