from django.db import models
from django.conf import settings


class SolicitudVacaciones(models.Model):

    empleado = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='solicitudes_vacaciones'
    )

    fecha_inicio = models.DateField()

    fecha_termino = models.DateField()

    motivo = models.TextField(max_length=500)

    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.empleado.username} - {self.fecha_inicio}"