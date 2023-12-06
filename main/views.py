from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializer import ShopUnitImport, ShopUnitGet
from .models import ShopUnit
from .validator import validate_uuid

# Create your views here.
class ImportAPI(APIView):
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
            instance = ShopUnit.objects.filter(id=item['id']).first()
            instance.update_parent_date()
        return Response("OK", status=200)
    

class DeleteUnitAPI(APIView):
    def delete(self, request, id):
        if not validate_uuid(id):
            return Response('Validation error', status=400)
        instanse = ShopUnit.objects.filter(id = id).first()
        if not instanse:
            return Response('Not found', status=404)
        instanse.delete()
        return Response('OK', status=200)
    
class NotesAPI(APIView):
    def get(self, request, id):
        if not validate_uuid(id):
            return Response('Validate error', status=400)
        instance = ShopUnit.objects.filter(id=id).first()
        if not instance:
            return Response('Not found', status=404)
        serialized_unit = ShopUnitGet(instance)
        instance.change_price_recursive()
        return Response(serialized_unit.data)