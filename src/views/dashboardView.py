import flet as ft


def DashboardView(page, tarea_controller):
    usuario_actual = getattr(page, "user_data", None)
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True, spacing=10)

    def notificar(texto):
        notif = ft.SnackBar(ft.Text(texto, color=ft.Colors.WHITE), bgcolor=ft.Colors.with_opacity(0.9, "#9D00FF"), open=True)
        page.overlay.append(notif)
        page.update()

    def borrar(id_tarea):
        exito, mensaje = tarea_controller.eliminar_tarea(id_tarea)
        if exito:
            cargar_tareas()
        else:
            notificar(mensaje)

    def cargar_tareas():
        if not (usuario_actual and "id_usuario" in usuario_actual):
            return
        lista_tareas.controls.clear()
        tareas = tarea_controller.obtener_lista(usuario_actual["id_usuario"])
        for tarea in tareas:
            lista_tareas.controls.append(
                ft.Container(
                    padding=14,
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
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Column(
                                spacing=4,
                                expand=True,
                                controls=[
                                    ft.Text(tarea["titulo"], weight="bold", size=14, color="#9D00FF"),
                                    ft.Text(tarea.get("descripcion", ""), size=12, color="#AAAAAA"),
                                    ft.Container(
                                        padding=ft.padding.only(top=4),
                                        content=ft.Row(
                                            spacing=8,
                                            controls=[
                                                ft.Container(
                                                    padding=ft.padding.symmetric(horizontal=10, vertical=4),
                                                    border_radius=12,
                                                    bgcolor=ft.Colors.with_opacity(0.2, "#9D00FF"),
                                                    border=ft.border.all(1, "#9D00FF"),
                                                    content=ft.Text(
                                                        tarea.get('prioridad','').capitalize(),
                                                        size=10,
                                                        color="#9D00FF",
                                                        weight="bold"
                                                    ),
                                                ),
                                                ft.Container(
                                                    padding=ft.padding.symmetric(horizontal=10, vertical=4),
                                                    border_radius=12,
                                                    bgcolor=ft.Colors.with_opacity(0.2, "#9D00FF"),
                                                    border=ft.border.all(1, "#9D00FF"),
                                                    content=ft.Text(
                                                        tarea.get('clasificacion',''),
                                                        size=10,
                                                        color="#9D00FF",
                                                        weight="bold"
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            ft.IconButton(
                                icon=ft.Icons.DELETE_ROUNDED,
                                icon_color="#9D00FF",
                                icon_size=22,
                                on_click=lambda e, id=tarea["id_tarea"]: borrar(id),
                            ),
                        ],
                    ),
                )
            )
        page.update()

    cargar_tareas()

    input_titulo = ft.TextField(
        label="Título",
        expand=True,
        border_radius=15,
        filled=True,
        bgcolor=ft.Colors.with_opacity(0.05, "#9D00FF"),
        border_color=ft.Colors.with_opacity(0.5, "#9D00FF"),
        focused_border_color="#9D00FF",
        label_style=ft.TextStyle(color="#9D00FF"),
        color=ft.Colors.WHITE,
    )
    input_descripcion = ft.TextField(
        label="Descripción",
        expand=True,
        border_radius=15,
        filled=True,
        bgcolor=ft.Colors.with_opacity(0.05, "#9D00FF"),
        border_color=ft.Colors.with_opacity(0.5, "#9D00FF"),
        focused_border_color="#9D00FF",
        label_style=ft.TextStyle(color="#9D00FF"),
        color=ft.Colors.WHITE,
    )
    select_prioridad = ft.Dropdown(
        label="Prioridad",
        width=120,
        border_radius=15,
        bgcolor=ft.Colors.with_opacity(0.05, "#9D00FF"),
        border_color=ft.Colors.with_opacity(0.5, "#9D00FF"),
        focused_border_color="#9D00FF",
        label_style=ft.TextStyle(color="#9D00FF"),
        color=ft.Colors.WHITE,
        options=[ft.dropdown.Option("alta"), ft.dropdown.Option("media"), ft.dropdown.Option("baja")],
        value="media"
    )
    select_categoria = ft.Dropdown(
        label="Categoría",
        width=120,
        border_radius=15,
        bgcolor=ft.Colors.with_opacity(0.05, "#9D00FF"),
        border_color=ft.Colors.with_opacity(0.5, "#9D00FF"),
        focused_border_color="#9D00FF",
        label_style=ft.TextStyle(color="#9D00FF"),
        color=ft.Colors.WHITE,
        options=[ft.dropdown.Option("Escuela"), ft.dropdown.Option("Trabajo"), ft.dropdown.Option("Cotidiano")],
        value="Escuela"
    )
    select_estado = ft.Dropdown(
        label="Estado",
        width=120,
        border_radius=15,
        bgcolor=ft.Colors.with_opacity(0.05, "#9D00FF"),
        border_color=ft.Colors.with_opacity(0.5, "#9D00FF"),
        focused_border_color="#9D00FF",
        label_style=ft.TextStyle(color="#9D00FF"),
        color=ft.Colors.WHITE,
        options=[ft.dropdown.Option("Pendiente"), ft.dropdown.Option("Terminada")],
        value="Pendiente"
    )

    def nueva_tarea(e):
        if not (usuario_actual and input_titulo.value):
            return
        tarea_controller.guardar_nueva(
            usuario_actual["id_usuario"], input_titulo.value, input_descripcion.value,
            select_prioridad.value, select_categoria.value, select_estado.value,
        )
        input_titulo.value = input_descripcion.value = ""
        select_prioridad.value = "media"
        select_categoria.value = "Escuela"
        select_estado.value = "Pendiente"
        cargar_tareas()

    nombre_usuario = usuario_actual['nombre'] if usuario_actual else 'Usuario'
    
    barra_superior = ft.Container(
        padding=ft.padding.only(left=16, right=16, top=12, bottom=8),
        bgcolor="#1A1A1A",
        border=ft.border.only(bottom=ft.BorderSide(2, "#9D00FF")),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(f"Hola, {nombre_usuario} ✨", size=18, weight="bold", color="#9D00FF"),
                ft.Row(
                    spacing=4,
                    controls=[
                        ft.IconButton(ft.Icons.PERSON_ROUNDED, icon_color="#9D00FF", on_click=lambda _: page.go("/perfil")),
                        ft.IconButton(ft.Icons.LOGOUT_ROUNDED, icon_color="#9D00FF", on_click=lambda _: page.go("/")),
                    ],
                ),
            ],
        ),
    )
    
    boton_agregar = ft.Container(
        width=45,
        height=45,
        border_radius=22,
        bgcolor="#9D00FF",
        content=ft.IconButton(ft.Icons.ADD_ROUNDED, icon_color=ft.Colors.BLACK, on_click=nueva_tarea),
    )
    
    formulario_tarea = ft.Container(
        padding=16,
        border_radius=20,
        bgcolor="#1A1A1A",
        border=ft.border.all(2, "#9D00FF"),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=20,
            color=ft.Colors.with_opacity(0.4, "#9D00FF"),
            offset=ft.Offset(0, 0),
        ),
        content=ft.Column(
            spacing=10,
            controls=[
                ft.Text("✨ Nueva tarea", size=14, color="#9D00FF", weight="bold"),
                input_titulo,
                input_descripcion,
                ft.Row(spacing=8, controls=[select_prioridad, select_categoria, select_estado, boton_agregar]),
            ],
        ),
    )

    return ft.View(
        route="/dashboard",
        bgcolor="#0A0A0A",
        controls=[
            barra_superior,
            ft.Container(
                padding=16,
                expand=True,
                content=ft.Column(
                    expand=True,
                    spacing=12,
                    controls=[
                        formulario_tarea,
                        ft.Text("📋 Mis tareas", size=15, weight="bold", color="#9D00FF"),
                        lista_tareas,
                    ],
                ),
            ),
        ],
    )
