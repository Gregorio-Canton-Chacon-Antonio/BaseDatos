import flet as ft


def PerfilView(page, auth_controller):
    datos = getattr(page, "user_data", None) or {}

    def campo_dato(etiqueta, valor, icono):
        return ft.Container(
            padding=16,
            border_radius=18,
            bgcolor="#1A1A1A",
            border=ft.border.all(1, "#9D00FF"),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.3, "#9D00FF"),
                offset=ft.Offset(0, 0),
            ),
            content=ft.Row(
                spacing=12,
                controls=[
                    ft.Container(
                        width=40,
                        height=40,
                        border_radius=20,
                        bgcolor=ft.Colors.with_opacity(0.2, "#9D00FF"),
                        border=ft.border.all(1, "#9D00FF"),
                        content=ft.Icon(icono, size=22, color="#9D00FF"),
                    ),
                    ft.Column(
                        spacing=2,
                        expand=True,
                        controls=[
                            ft.Text(etiqueta, size=11, color="#888888"),
                            ft.Text(str(valor) if valor else "—", size=14, color="#FFFFFF", weight="w500"),
                        ],
                    ),
                ],
            ),
        )

    encabezado = ft.Container(
        padding=ft.padding.only(left=16, right=16, top=12, bottom=8),
        bgcolor="#1A1A1A",
        border=ft.border.only(bottom=ft.BorderSide(2, "#9D00FF")),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text("Mi perfil 👤", size=18, weight="bold", color="#9D00FF"),
                ft.Row(
                    spacing=4,
                    controls=[
                        ft.IconButton(ft.Icons.CHECKLIST_ROUNDED, icon_color="#9D00FF", on_click=lambda _: page.go("/dashboard")),
                        ft.IconButton(ft.Icons.LOGOUT_ROUNDED, icon_color="#9D00FF", on_click=lambda _: page.go("/")),
                    ],
                ),
            ],
        ),
    )
    
    avatar_usuario = ft.Container(
        width=80,
        height=80,
        border_radius=40,
        bgcolor=ft.Colors.with_opacity(0.2, "#9D00FF"),
        border=ft.border.all(2, "#9D00FF"),
        content=ft.Icon(ft.Icons.PERSON_ROUNDED, size=45, color="#9D00FF"),
    )
    
    nombre_usuario = ft.Text(datos.get("nombre", "Usuario"), size=22, weight="bold", color="#9D00FF")
    email_usuario = ft.Text(datos.get("email", ""), size=13, color="#888888")
    
    tarjeta_perfil = ft.Container(
        padding=20,
        border_radius=25,
        bgcolor="#1A1A1A",
        border=ft.border.all(2, "#9D00FF"),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=25,
            color=ft.Colors.with_opacity(0.5, "#9D00FF"),
            offset=ft.Offset(0, 0),
        ),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
            controls=[avatar_usuario, nombre_usuario, email_usuario],
        ),
    )
    
    espacio = ft.Divider(height=8, color=ft.Colors.TRANSPARENT)

    return ft.View(
        route="/perfil",
        bgcolor="#0A0A0A",
        controls=[
            encabezado,
            ft.Container(
                padding=20,
                content=ft.Column(
                    spacing=12,
                    controls=[
                        tarjeta_perfil,
                        espacio,
                        campo_dato("Apellido", datos.get("apellido"), ft.Icons.BADGE_OUTLINED),
                        campo_dato("Teléfono", datos.get("telefono"), ft.Icons.PHONE_ROUNDED),
                        campo_dato("Fecha de registro", datos.get("fecha_registro"), ft.Icons.CALENDAR_TODAY_ROUNDED),
                    ],
                ),
            ),
        ],
    )
