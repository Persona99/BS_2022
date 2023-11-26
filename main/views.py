from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializer import ShopUnitImport
from .models import ShopUnit


# Create your views here.
class Import_api(APIView):
    def post(self, request):
        for item in request.data['items']:
            instance = ShopUnit.objects.filter(id=item['id']).first()
            unit = ShopUnitImport(instance, data=item)
            if not unit.is_valid():
                return Response(unit.errors, status=400)
            unit.save()
        return Response("OK", status=200)