
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .forms import PerfilEmpleadoForm, validar_rut
from .models import PerfilEmpleado


class PruebasSeguridadEmpleado(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(
            username="empleado_prueba",
            password="ClaveTemporalSegura123!"
        )

    def test_rut_valido(self):
        resultado = validar_rut("12.345.678-5")
        self.assertEqual(resultado, "12345678-5")

    def test_rut_invalido(self):
        from django import forms

        with self.assertRaises(forms.ValidationError):
            validar_rut("12.345.678-9")

    def test_correo_invalido(self):
        formulario = PerfilEmpleadoForm(
            data={
                "rut": "12.345.678-5",
                "email": "correo-invalido",
                "telefono": "+56912345678",
            },
            usuario=self.usuario
        )

        self.assertFalse(formulario.is_valid())
        self.assertIn("email", formulario.errors)

    def test_telefono_invalido(self):
        formulario = PerfilEmpleadoForm(
            data={
                "rut": "12.345.678-5",
                "email": "prueba@example.com",
                "telefono": "123abc",
            },
            usuario=self.usuario
        )

        self.assertFalse(formulario.is_valid())
        self.assertIn("telefono", formulario.errors)

    def test_rut_duplicado(self):
        otro_usuario = User.objects.create_user(
            username="otro_empleado",
            password="OtraClaveTemporal123!"
        )

        PerfilEmpleado.objects.create(
            usuario=otro_usuario,
            rut="12345678-5",
            telefono="+56987654321"
        )

        formulario = PerfilEmpleadoForm(
            data={
                "rut": "12.345.678-5",
                "email": "prueba@example.com",
                "telefono": "+56912345678",
            },
            usuario=self.usuario
        )

        self.assertFalse(formulario.is_valid())
        self.assertIn("rut", formulario.errors)

    def test_perfil_requiere_autenticacion(self):
        respuesta = self.client.get(reverse("perfil"))

        self.assertEqual(respuesta.status_code, 302)
        self.assertIn("/login/", respuesta.url)

    def test_perfil_autenticado(self):
        self.client.force_login(self.usuario)

        respuesta = self.client.get(reverse("perfil"))

        self.assertEqual(respuesta.status_code, 200)
