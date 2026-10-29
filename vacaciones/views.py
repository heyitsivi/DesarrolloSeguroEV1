from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SolicitudVacacionesForm
from .models import SolicitudVacaciones


@login_required
def solicitar_vacaciones(request):

    if request.method == 'POST':
        formulario = SolicitudVacacionesForm(request.POST)

        if formulario.is_valid():
            solicitud = formulario.save(commit=False)
            solicitud.empleado = request.user
            solicitud.save()

            return redirect('mis_solicitudes')

    else:
        formulario = SolicitudVacacionesForm()

    return render(
        request,
        'vacaciones/solicitar_vacaciones.html',
        {'formulario': formulario}
    )


@login_required
def mis_solicitudes(request):

    solicitudes = SolicitudVacaciones.objects.filter(
        empleado=request.user
    ).order_by('-fecha_solicitud')

    return render(
        request,
        'vacaciones/mis_solicitudes.html',
        {'solicitudes': solicitudes}
    )