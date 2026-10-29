from django.conf import settings
from django.db import models


class PerfilEmpleado(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_empleado'
    )
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.rut}"