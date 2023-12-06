from django.db import models
from enum import Enum

types = (
    ('OFFER', 'OFFER'),
    ('CATEGORY', 'CATEGORY')
)

# Create your models here.
class ShopUnit(models.Model):
    id = models.UUIDField(null=False, primary_key=True)
    name = models.CharField(max_length=100,null=False)
    date = models.DateTimeField(null=False)
    parentId = models.ForeignKey('ShopUnit', on_delete=models.CASCADE, null=True, default=None, blank=True, related_name='children')
    type = models.CharField(max_length=100, choices=types, null=False)
    price = models.BigIntegerField(null=True, default=None, blank=True)
    
    def update_parent_date(self):
        parent = self
        while parent.parentId:
            parent = ShopUnit.objects.filter(id = parent.parentId.id).first()
            parent.date = self.date
            parent.save()
    
    def change_price_recursive(self):
        children = ShopUnit.objects.filter(parentId=self.id).all()
        if not children:
            return {'sum': self.price, 'count': 1}
        res = {'sum': 0, 'count': 0}
        for child in children:
            qs = child.change_price_recursive()
            res['sum'] += qs['sum']
            res['count'] += qs['count']
        self.price = res['sum'] / res['count']
        self.save()
        return res