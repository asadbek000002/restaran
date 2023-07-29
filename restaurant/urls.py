from django.urls import path, include
from rest_framework import routers
from .views import *

urlpatterns = [
    path('menu/', MenuViewSet.as_view({'get': 'list'}), name='menu'),
    path('buy/', BuyViewSet.as_view({'get': 'list'}), name='buy'),
    path('products/', ProductsViewSet.as_view({'get': 'list'}), name='products'),
]
