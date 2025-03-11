from django.urls import path
from . import views

urlpatterns = [
    path('registro-clientes/', views.registro_clientes, name='registro_clientes'),
    path('registro-empleados/', views.registro_empleados, name='registro_empleados'),   
]