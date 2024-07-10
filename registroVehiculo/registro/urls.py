from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form_persona/', views.formPersona, name='formPersona'),
    path('list_persona/', views.listPersona, name='listPersona'),
    path('form_vehiculo/', views.formVehiculo, name='formVehiculo'),
    path('list_vehiculo/', views.listVehiculo, name='listVehiculo'),
]