from django import forms
from .models import Clientes, Empleados, Rol, Turno  

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'tipo_empresa']

class EmpleadosForm(forms.ModelForm):
    rol = forms.ModelChoiceField(
        queryset=Rol.objects.all(),
        empty_label="Selecciona Rol"
    )

    class Meta:
        model = Empleados
        fields = ['nombre', 'rol']
        widgets = {
            'rol': forms.Select(attrs={'class': 'form-control'})
        }

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['empleado', 'fecha', 'hora_inicio', 'hora_fin']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            }