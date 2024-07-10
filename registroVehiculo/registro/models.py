from django.db import models

from .validators import validarFecha

# Create your models here.
class Persona(models.Model):
    idPersona = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10, null=False, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    fechaNacimiento = models.DateField(validators=[validarFecha])

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
class Vehiculo(models.Model):
    idVehiculo = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=6, unique=True, null=False)
    marca = models.CharField(max_length=50, null=False)
    modelo = models.CharField(max_length=50, null=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente + ' ' + self.marca