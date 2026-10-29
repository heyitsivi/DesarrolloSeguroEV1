from django.urls import path
from . import views

urlpatterns = [
    path(
        'solicitar/',
        views.solicitar_vacaciones,
        name='solicitar_vacaciones'
    ),

    path(
        'mis-solicitudes/',
        views.mis_solicitudes,
        name='mis_solicitudes'
    ),
]