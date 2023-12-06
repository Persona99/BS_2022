from django.urls import path
from . import views 

urlpatterns = [
    path('imports', views.ImportAPI.as_view()),
    path('delete/<str:id>', views.DeleteUnitAPI.as_view()),
    path('nodes/<str:id>', views.NotesAPI.as_view()),
]
