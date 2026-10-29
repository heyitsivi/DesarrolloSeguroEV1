from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render

from .forms import PerfilEmpleadoForm
from .models import PerfilEmpleado


@login_required
def perfil(request):
    empleado = PerfilEmpleado.objects.filter(
        usuario=request.user
    ).first()

    datos_iniciales = {
        "rut": empleado.rut if empleado else "",
        "email": request.user.email,
        "telefono": empleado.telefono if empleado else "",
    }

    guardado = False

    if request.method == "POST":
        formulario = PerfilEmpleadoForm(
            request.POST,
            usuario=request.user
        )

        if formulario.is_valid():
            with transaction.atomic():
                PerfilEmpleado.objects.update_or_create(
                    usuario=request.user,
                    defaults={
                        "rut": formulario.cleaned_data["rut"],
                        "telefono": formulario.cleaned_data["telefono"],
                    }
                )

                request.user.email = formulario.cleaned_data["email"]
                request.user.save(update_fields=["email"])

            guardado = True
    else:
        formulario = PerfilEmpleadoForm(
            initial=datos_iniciales,
            usuario=request.user
        )

    return render(request, "empleados/perfil.html", {
        "formulario": formulario,
        "guardado": guardado,
    })