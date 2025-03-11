from django.db import models

class Rol(models.Model):
    cargo = models.CharField(max_length=100)

    class Meta:
        db_table = 'rol'

    def __str__(self):
        return self.cargo

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_empresa = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return self.nombre

class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        db_table = 'empleados'
    def __str__(self):
        return self.nombre
