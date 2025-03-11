from django import forms
from .models import Clientes, Empleados, Rol  # Asegúrate de importar Rol

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
