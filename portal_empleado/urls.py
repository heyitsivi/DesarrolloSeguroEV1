from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='empleados/login.html'
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path('', include('empleados.urls')),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.BASE_DIR / 'empleados' / 'static'
)