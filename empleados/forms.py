import re

from django import forms
from django.contrib.auth.models import User

from .models import PerfilEmpleado


def validar_rut(rut):
    rut = rut.upper().replace(".", "").replace("-", "").strip()

    if not re.fullmatch(r"\d{7,8}[0-9K]", rut):
        raise forms.ValidationError("El formato del RUT no es válido.")

    cuerpo = rut[:-1]
    digito = rut[-1]

    suma = 0
    multiplicador = 2

    for numero in reversed(cuerpo):
        suma += int(numero) * multiplicador
        multiplicador = 2 if multiplicador == 7 else multiplicador + 1

    resultado = 11 - (suma % 11)
    verificador = "0" if resultado == 11 else "K" if resultado == 10 else str(resultado)

    if digito != verificador:
        raise forms.ValidationError("El dígito verificador del RUT es incorrecto.")

    return f"{cuerpo}-{digito}"


class PerfilEmpleadoForm(forms.Form):
    rut = forms.CharField(max_length=12, label="RUT")
    email = forms.EmailField(label="Correo electrónico")
    telefono = forms.CharField(max_length=12, label="Teléfono")

    def clean_rut(self):
        rut = validar_rut(self.cleaned_data["rut"])

        if PerfilEmpleado.objects.filter(rut=rut).exclude(
            usuario=self.usuario
        ).exists():
            raise forms.ValidationError("Este RUT ya está registrado.")

        return rut

    def clean_telefono(self):
        telefono = self.cleaned_data["telefono"].strip()

        if not re.fullmatch(r"\+569\d{8}", telefono):
            raise forms.ValidationError(
                "El teléfono debe tener formato +56912345678."
            )

        return telefono

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = usuario