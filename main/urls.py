from django.urls import path
from . import views 

urlpatterns = [
    path('imports', views.Import_api.as_view())
]
