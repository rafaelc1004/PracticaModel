

from datetime import date

from django.forms import ValidationError


def validarFecha(fecha):

    fechaLimite = (date.today().year - 18)
    if(fecha > fechaLimite):
        raise ValidationError(f'La fecha debe ser anterior a {fechaLimite}.')

