import flet as ft

def LoginView(page: ft.Page, auth_controller):
    snack = ft.SnackBar(content=ft.Text(""))
    page.overlay.append(snack)

    avatar = ft.CircleAvatar(
        radius=45,
        bgcolor="#9e9e9e",
        content=ft.Icon(ft.Icons.PERSON, size=50, color="white")
    )

    email_input = ft.TextField(
        label="Correo electrónico",
        width=260,
        border_radius=8,
        border_color="#757575",
        focused_border_color="#424242",
        keyboard_type=ft.KeyboardType.EMAIL
    )

    pass_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=260,
        border_radius=8,
        border_color="#757575",
        focused_border_color="#424242",
    )

    def login_click(e):
        error = False
        if not email_input.value.strip():
            email_input.error_text = "El correo es obligatorio"
            error = True
        else:
            email_input.error_text = None

        if not pass_input.value.strip():
            pass_input.error_text = "La contraseña es obligatoria"
            error = True
        else:
            pass_input.error_text = None

        if error:
            snack.content = ft.Text("Debes completar los campos")
            snack.open = True
            page.update()
            return

        user, msg = auth_controller.login(email_input.value, pass_input.value)
        print(f"login result: {user}, {msg}")

        if user:
            page.session.set("user", user)
            page.push_route("/dashboard")
        else:
            snack.content = ft.Text(msg)
            snack.open = True
            page.update()

    pass_input.on_submit = login_click

    formulario = ft.Container(
        content=ft.Column(
            [
                avatar,
                ft.Text("Iniciar Sesión", size=26, weight=ft.FontWeight.BOLD, color="#212121"),
                email_input,
                pass_input,
                ft.ElevatedButton(
                    "Entrar",
                    on_click=login_click,
                    style=ft.ButtonStyle(
                        bgcolor="#616161",
                        color="white",
                        shape=ft.RoundedRectangleBorder(radius=8)
                    )
                ),
                ft.TextButton(
                    "Crear una nueva cuenta",
                    on_click=lambda _: page.push_route("/registro")
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        padding=30,
        bgcolor="#fafafa",
        border_radius=12,
        shadow=ft.BoxShadow(blur_radius=8, color="#9e9e9e")
    )

    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor="#e0e0e0",
        controls=[formulario]
    )
