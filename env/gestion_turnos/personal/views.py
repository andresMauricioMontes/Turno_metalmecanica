from django.shortcuts import render, redirect
from .forms import ClientesForm, EmpleadosForm
from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Bienvenido a Gestión de Turnos!"),

def registro_clientes(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('registro_clientes')
        else:
            print(form.errors)
    else:
        form = ClientesForm()
    return render(request, 'registro_clientes.html', {'form': form})

def registro_empleados(request):
    if request.method == 'POST':
        form = EmpleadosForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('registro_empleados')
        else:
            print(form.errors)
    else:
        form = EmpleadosForm()
    return render(request, 'registro_empleados.html', {'form': form})
