
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
                    'maxlength': 500,
                    'placeholder': 'Ingrese el motivo de sus vacaciones'
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_termino = cleaned_data.get('fecha_termino')

        if fecha_inicio and fecha_termino:
            if fecha_termino < fecha_inicio:
                self.add_error(
                    'fecha_termino',
                    'La fecha de término no puede ser anterior a la fecha de inicio.'
                )

        return cleaned_data
