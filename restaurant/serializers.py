from rest_framework import serializers
from .models import *




class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
    
    

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    
    

class BuySerializers(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = "__all__"