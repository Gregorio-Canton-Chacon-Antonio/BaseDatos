import flet as ft


def LoginView(page: ft.Page, auth_controller):

    def mostrar_password(e):
        password_field.password = not password_field.password
        password_field.update()

    def mensaje_error(texto):
        snackbar = ft.SnackBar(ft.Text(texto, color=ft.Colors.WHITE), bgcolor=ft.Colors.with_opacity(0.9, "#9D00FF"), open=True)
        page.overlay.append(snackbar)
        page.update()

    email_field = ft.TextField(
        label="Correo",
        border_radius=20,
        filled=True,
        bgcolor=ft.Colors.with_opacity(0.05, "#9D00FF"),
        border_color=ft.Colors.with_opacity(0.5, "#9D00FF"),
        focused_border_color="#9D00FF",
        label_style=ft.TextStyle(color="#9D00FF"),
        color=ft.Colors.WHITE,
    )
    password_field = ft.TextField(
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
            on_click=mostrar_password
        ),
    )

    def hacer_login(e):
        if not email_field.value or not password_field.value:
            mensaje_error("Completa todos los campos")
            return
        try:
            usuario, msg = auth_controller.login(email_field.value, password_field.value)
            if usuario:
                page.user_data = usuario
                page.go("/dashboard")
            else:
                mensaje_error(msg)
        except Exception as error:
            mensaje_error(f"Error: {str(error)}")
            print(f"Error en login: {error}")

    icono_principal = ft.Container(
        width=70,
        height=70,
        border_radius=35,
        bgcolor=ft.Colors.with_opacity(0.2, "#9D00FF"),
        border=ft.border.all(2, "#9D00FF"),
        content=ft.Icon(ft.Icons.TASK_ALT_ROUNDED, size=40, color="#9D00FF"),
    )
    
    titulo_app = ft.Text("Gestor de Tareas", size=24, weight="bold", color="#9D00FF")
    subtitulo = ft.Text("Inicia sesión", size=13, color="#888888")
    espaciador = ft.Divider(height=8, color=ft.Colors.TRANSPARENT)
    
    btn_login = ft.Container(
        content=ft.ElevatedButton(
            "Entrar",
            width=290,
            height=45,
            style=ft.ButtonStyle(
                bgcolor="#9D00FF",
                color=ft.Colors.BLACK,
                shape=ft.RoundedRectangleBorder(radius=20),
            ),
            on_click=hacer_login
        ),
    )
    
    btn_registro = ft.TextButton(
        "¿Sin cuenta? Regístrate",
        style=ft.ButtonStyle(color="#9D00FF"),
        on_click=lambda _: page.go("/registro")
    )

    return ft.View(
        route="/",
        bgcolor="#0A0A0A",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(
                width=360,
                padding=35,
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
                    spacing=18,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        icono_principal,
                        titulo_app,
                        subtitulo,
                        espaciador,
                        email_field,
                        password_field,
                        btn_login,
                        btn_registro,
                    ],
                ),
            )
        ],
    )
