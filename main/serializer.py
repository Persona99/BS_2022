from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.response import Response
from .models import ShopUnit
from datetime import datetime

class ShopUnitImport(serializers.ModelSerializer):
    class Meta:
        model = ShopUnit
        fields = ['id', 'name', 'parentId', 'type', 'price', 'date']
    
    def update(self, instance: ShopUnit, validated_data):
        instance.clean_fields()
        return super().update(instance, validated_data)

    def validate(self, data):
        if 'parentId' in data and data.get('parentId'):
            parent = ShopUnit.objects.get(id = data.get('parentId').id)
            if parent.type != 'CATEGORY':
                raise serializers.ValidationError('Parrent is not a category')

        if data.get('type') == 'CATEGORY' and data.get('price'):
            raise serializers.ValidationError("Not need price for category")
        if data.get('type') == 'CATEGORY':
            data.update({'price': None})
        if data.get('type') == "OFFER" and not data.get('price'):
            raise serializers.ValidationError("Need price for offer")
        if data.get('type') == "OFFER" and ShopUnit.objects.filter(parentId = data.get('id')).first():
            raise serializers.ValidationError("Offer cant has child")
        return data

    def validated_date(self, value):
        try:
            datetime.fromisoformat(value)
        except:
            raise serializers.ValidationError('Wrong date format') 
        return value
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Price is less than 0')
        return value
    

class ShopUnitDelete(serializers.Serializer):
    id = serializers.UUIDField()