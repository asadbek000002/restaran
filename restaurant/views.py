from .serializers import *
from .models import *
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
     
class BuyViewSet(viewsets.ModelViewSet):
    queryset = Buy.objects.all()
    serializer_class = BuySerializers
    
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
    
    