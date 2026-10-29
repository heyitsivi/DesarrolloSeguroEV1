
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    # Redirigir la página principal al login
    path(
        '',
        RedirectView.as_view(
            pattern_name='login',
            permanent=False
        ),
        name='inicio'
    ),

    # Panel de administración
    path('admin/', admin.site.urls),

    # Inicio de sesión
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='empleados/login.html'
        ),
        name='login'
    ),

    path('vacaciones/', include('vacaciones.urls')),
=======

    # Cierre de sesión

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # Rutas del módulo de empleados
    path('', include('empleados.urls')),
]

# Archivos estáticos durante el desarrollo
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.BASE_DIR / 'empleados' / 'static'
)
