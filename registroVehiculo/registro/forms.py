

from django import forms
from .models import Persona, Vehiculo


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        labels ={
            'rut':'Rut',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'fechaNacimiento':'Fecha de Nacimiento'
        }

class VehiculoForm(forms.ModelForm):
        patente = forms.CharField(label='Patente', max_length=6)
        marca = forms.CharField(label='Marca', max_length=50)
        modelo = forms.CharField(label='Modelo', max_length=50)
        persona = forms.ModelChoiceField(queryset=Persona.objects.all(), label="Propietario", widget=forms.Select())