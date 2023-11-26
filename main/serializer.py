from rest_framework import serializers
from rest_framework.response import Response
from .models import ShopUnit
from datetime import datetime

class ShopUnitImport(serializers.ModelSerializer):
    class Meta:
        model = ShopUnit
        fields = ['id', 'name', 'parentId', 'type', 'price', 'date']
    
