from django.urls import path
from . import views

urlpatterns = [
   # en urls.py
path('registro-clientes/', views.registro_clientes, name='registro_clientes'),
path('registro-empleados/', views.registro_empleados, name='registro_empleados'),
path('asignar-turno/', views.asignar_turno, name='asignar_turno'),
path('listar-turnos/', views.listar_turnos, name='listar_turnos'),

]


