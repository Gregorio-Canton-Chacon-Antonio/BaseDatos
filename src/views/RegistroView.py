import flet as ft
from datetime import datetime


def RegistroView(page: ft.Page, auth_controller):

    def toggle_pass(e):
        password_input.password = not password_input.password
        password_input.update()

    def notificar(texto):
        notificacion = ft.SnackBar(ft.Text(texto, color=ft.Colors.WHITE), bgcolor=ft.Colors.with_opacity(0.9, "#9D00FF"), open=True)
        page.overlay.append(notificacion)
        page.update()

    nombre_input = ft.TextField(
        label="Nombre",
        border_radius=20,
        filled=True,
        bgcolor=ft.Colors.with_opacity(0.05, "#9D00FF"),
        border_color=ft.Colors.with_opacity(0.5, "#9D00FF"),
        focused_border_color="#9D00FF",
        label_style=ft.TextStyle(color="#9D00FF"),
        color=ft.Colors.WHITE,
    )
    telefono_input = ft.TextField(
        label="Teléfono",
        border_radius=20,
        filled=True,
        bgcolor=ft.Colors.with_opacity(0.05, "#9D00FF"),
        border_color=ft.Colors.with_opacity(0.5, "#9D00FF"),
        focused_border_color="#9D00FF",
        label_style=ft.TextStyle(color="#9D00FF"),
        color=ft.Colors.WHITE,
    )
    email_input = ft.TextField(
        label="Correo",
        border_radius=20,
        filled=True,
        bgcolor=ft.Colors.with_opacity(0.05, "#9D00FF"),
        border_color=ft.Colors.with_opacity(0.5, "#9D00FF"),
        focused_border_color="#9D00FF",
        label_style=ft.TextStyle(color="#9D00FF"),
        color=ft.Colors.WHITE,
    )
    password_input = ft.TextField(
        label="Contraseña",
        password=True,
        border_radius=20,
        filled=True,
        bgcolor=ft.Colors.with_opacity(0.05, "#9D00FF"),
        border_color=ft.Colors.with_opacity(0.5, "#9D00FF"),
        focused_border_color="#9D00FF",
        label_style=ft.TextStyle(color="#9D00FF"),
        color=ft.Colors.WHITE,
        suffix=ft.IconButton(
            icon=ft.Icons.VISIBILITY_OUTLINED,
            icon_color="#9D00FF",
            on_click=toggle_pass
        ),
    )

    def crear_usuario(e):
        if not nombre_input.value or not email_input.value or not password_input.value:
            notificar("Completa los campos obligatorios")
            return
        try:
            fecha_hoy = datetime.now().strftime("%Y-%m-%d")
            tel = telefono_input.value or ""
            resultado, mensaje = auth_controller.registrar_Usuario(
                nombre_input.value, "", email_input.value, password_input.value, tel, fecha_hoy
            )
            if resultado:
                notificar("Usuario registrado correctamente")
                page.go("/")
            else:
                notificar(mensaje)
        except Exception as ex:
            notificar(f"Error: {str(ex)}")
            print(f"Error en registro: {ex}")

    icono_usuario = ft.Container(
        width=60,
        height=60,
        border_radius=30,
        bgcolor=ft.Colors.with_opacity(0.2, "#9D00FF"),
        border=ft.border.all(2, "#9D00FF"),
        content=ft.Icon(ft.Icons.PERSON_ADD_ROUNDED, size=35, color="#9D00FF"),
    )
    
    titulo = ft.Text("Crear cuenta", size=22, weight="bold", color="#9D00FF")
    separador = ft.Divider(height=6, color=ft.Colors.TRANSPARENT)
    
    boton_crear = ft.Container(
        content=ft.ElevatedButton(
            "Registrarse",
            width=290,
            height=45,
            style=ft.ButtonStyle(
                bgcolor="#9D00FF",
                color=ft.Colors.BLACK,
                shape=ft.RoundedRectangleBorder(radius=20),
            ),
            on_click=crear_usuario
        ),
    )
    
    link_login = ft.TextButton(
        "Ya tengo cuenta",
        style=ft.ButtonStyle(color="#9D00FF"),
        on_click=lambda _: page.go("/")
    )

    return ft.View(
        route="/registro",
        bgcolor="#0A0A0A",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(
                width=360,
                padding=30,
                border_radius=25,
                bgcolor="#1A1A1A",
                border=ft.border.all(2, "#9D00FF"),
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=30,
                    color=ft.Colors.with_opacity(0.5, "#9D00FF"),
                    offset=ft.Offset(0, 0),
                ),
                content=ft.Column(
                    tight=True,
                    spacing=14,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        icono_usuario,
                        titulo,
                        separador,
                        nombre_input,
                        telefono_input,
                        email_input,
                        password_input,
                        boton_crear,
                        link_login,
                    ],
                ),
            )
        ],
    )
