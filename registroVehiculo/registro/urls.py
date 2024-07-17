from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form_persona/', views.formPersona, name='formPersona'),
    path('form_persona/<int:id>/', views.formPersona, name='updatePersona'),
    path('list_persona/', views.listPersona, name='listPersona'),
    path('del_persona/<int:id>/', views.delPersona, name='delPersona'),
    path('form_vehiculo/', views.formVehiculo, name='formVehiculo'),
    path('form_vehiculo/<int:id>/', views.formVehiculo, name='updateVehiculo'),
    path('list_vehiculo/', views.listVehiculo, name='listVehiculo'),
    path('del_vehiculo/<int:id>/', views.delVehiculo, name='delVehiculo'),
    path('list_car_people/<int:id>/', views.listVehiculoPersona, name='listCarPeople'),

]
