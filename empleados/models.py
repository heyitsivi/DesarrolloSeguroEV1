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
        rut_oculto = f"******{self.rut[-4:]}" if self.rut else "Sin RUT"
        return f"{self.usuario.username} - {rut_oculto}"