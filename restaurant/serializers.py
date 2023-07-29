from rest_framework import serializers
from .models import *




class MenuSerializers(serializers.ModelSerializer):
    
    model = Menu
    fields = "__all__"
    
    

class ProductSerializers(serializers.ModelSerializer):
    
    model = Product
    fields = "__all__"
    
    

class BuySerializers(serializers.ModelSerializer):
    
    model = Buy
    fields = "__all__"