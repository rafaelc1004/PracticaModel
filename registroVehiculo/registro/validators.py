from datetime import date, timedelta

from django.forms import ValidationError

def validarFecha(value):

    fechaLimite = date.today().replace(year=date.today().year - 18)
    print("mi fecha",fechaLimite)
    print("mi fecha2",value)
    if (value > fechaLimite):
        raise ValidationError("Persona es menor de edad!")