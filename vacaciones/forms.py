from django import forms
from .models import SolicitudVacaciones


class SolicitudVacacionesForm(forms.ModelForm):

    class Meta:
        model = SolicitudVacaciones

        fields = [
            'fecha_inicio',
            'fecha_termino',
            'motivo',
        ]

        labels = {
            'fecha_inicio': 'Fecha de inicio',
            'fecha_termino': 'Fecha de término',
            'motivo': 'Motivo de la solicitud',
        }

        widgets = {
            'fecha_inicio': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),

            'fecha_termino': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),

            'motivo': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Ingrese el motivo de sus vacaciones'
                }
            ),
        }