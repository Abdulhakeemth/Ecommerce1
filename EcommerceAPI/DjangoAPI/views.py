from django.shortcuts import render
from rest_framework import generics
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from .models import  Category,Book,Product
from .serializers import CategorySerializer,BookSerializer,ProductSerializer
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    UserModel View.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
class ListCategory(generics.ListCreateAPIView):
    queryset  = Category.objects.all()
    serializer_class = CategorySerializer
    # def post(self, request, format=None):
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Category.objects.all()
    serializer_class = CategorySerializer 

class ListBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer   



class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  
 
class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    