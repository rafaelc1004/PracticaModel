

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
        widgets = {
            'fechaNacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class VehiculoForm(forms.ModelForm):
    patente = forms.CharField(label='Patente', max_length=6)
    marca = forms.CharField(label='Marca', max_length=50)
    modelo = forms.CharField(label='Modelo', max_length=50)
    persona = forms.ModelChoiceField(queryset=Persona.objects.all(), label="Propietario", widget=forms.Select())

    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'persona']

    def __init__(self, *args, **kwargs):
        super(VehiculoForm, self).__init__(*args, **kwargs)
        self.fields['persona'].empty_label = "Seleccione una opcion"
        self.fields['patente'].required = False