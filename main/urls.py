from django.urls import path
from . import views 

urlpatterns = [
    path('imports', views.Import_api.as_view()),
    path('delete/<str:id>', views.Delete_unit_api.as_view()),
    path('nodes/<str:id>', views.Notes_api.as_view())
]
