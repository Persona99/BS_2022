from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializer import ShopUnitImport, ShopUnitUUid, ShopUnitGet
from .models import ShopUnit


# Create your views here.
class Import_api(APIView):
    def post(self, request):
        if 'updateDate' not in request.data:
            return Response(status=400)
        for item in request.data['items']:
            instance = ShopUnit.objects.filter(id=item['id']).first()
            item['date'] = request.data['updateDate']
            unit = ShopUnitImport(instance, data=item)
            if not unit.is_valid():
                return Response(unit.errors, status=400)
            unit.save()
        return Response("OK", status=200)
    

class Delete_unit_api(APIView):
    def delete(self, request, id):
        serializer = ShopUnitUUid(data={'id':id})
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        instanse = ShopUnit.objects.filter(id = id).first()
        if not instanse:
            return Response('Not found', status=404)
        instanse.delete()
        return Response('OK', status=200)
    
class Notes_api(APIView):
    def get(self, request , id):
        serialized_id = ShopUnitUUid(data={'id': id})
        if not serialized_id.is_valid():
            return Response(serialized_id.errors, status=400)
        instance = ShopUnit.objects.filter(id=id).first()
        if not instance:
            return Response('Not found', status=404)
        
        serialized_unit = ShopUnitGet(instance)
        return Response(serialized_unit.data)