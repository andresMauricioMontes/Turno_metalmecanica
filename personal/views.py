from django.shortcuts import render, redirect
from .forms import ClientesForm, EmpleadosForm
from django.http import HttpResponse
from django.contrib import messages  # Importa el sistema de mensajes

def home(request):
    return HttpResponse("¡Bienvenido a Gestión de Turnos!")

def registro_clientes(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente registrado con éxito.')  # Mensaje de éxito
            return redirect('registro_clientes')
        else:
            messages.error(request, 'Hubo un error al registrar el cliente.')  # Mensaje de error
    else:
        form = ClientesForm()
    return render(request, 'registro_clientes.html', {'form': form})

def registro_empleados(request):
    if request.method == 'POST':
        form = EmpleadosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado registrado con éxito.')  # Mensaje de éxito
            return redirect('registro_empleados')
        else:
            messages.error(request, 'Hubo un error al registrar el empleado.')  # Mensaje de error
    else:
        form = EmpleadosForm()
    return render(request, 'registro_empleados.html', {'form': form})

from .models import Turno
from .forms import TurnoForm

def asignar_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Turno asignado con éxito.')
            return redirect('asignar_turno')
        else:
            messages.error(request, 'Error al asignar el turno.')
    else:
        form = TurnoForm()
    return render(request, 'asignar_turno.html', {'form': form})

from .models import Turno

def listar_turnos(request):
    turnos = Turno.objects.select_related('empleado').all()
    return render(request, 'listar_turnos.html', {'turnos': turnos})
