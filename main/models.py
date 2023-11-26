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
    parentId = models.UUIDField(null=True, default=None, blank=True)
    type = models.CharField(max_length=100, choices=types, null=False)
    price = models.BigIntegerField(null=True, default=None, blank=True)