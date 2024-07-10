from django.shortcuts import get_object_or_404, redirect, render
from .forms import PersonaForm, VehiculoForm

from .models import Persona, Vehiculo

# Create your views here.

def index(request):
    return render(request, "registro/index.html")

def formPersona(request, id=None):
    if (id):
        persona = get_object_or_404(Persona, idPersona=id)
    else:
        persona = Persona()

    if(request.method == 'POST'):
        form = PersonaForm(request.POST, instance=persona)
        if(form.is_valid()):
            form.save()
            return redirect('listPersona')
        else:
            print(form.errors)
    else:
        form = PersonaForm(instance=persona)
    
    return render(request, 'registro/form_persona.html', {'form': form})

def listPersona(request):
    personas = Persona.objects.all()
    return render(request, 'registro/list_persona.html', {'personas': personas})

def formVehiculo(request, id=None):
    if (id):
        vehiculo = get_object_or_404(Vehiculo, idVehiculo=id)
    else:
        vehiculo = Vehiculo()

    if(request.method == 'POST'):
        form = VehiculoForm(request.POST, instance = vehiculo)
        if(form.is_valid()):
            form.save()
            return redirect('listVehiculo')
        else:
            print(form.errors)
    else:
        form = VehiculoForm(instance=vehiculo)

        return render(request, 'registro/form_vehiculo.html', {'form':form})
    
def listVehiculo(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'registro/list_vehiculo.html', {'vehiculos':vehiculos})