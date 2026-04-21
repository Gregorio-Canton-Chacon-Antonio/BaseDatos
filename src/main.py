import flet as ft
from controllers.UserController import AuthController
from controllers.TareaController import TareaController
from views.LoginView import LoginView
from views.dashboard import DashboardView

def start(page: ft.Page):
    # Configuracion inicial de la pagina 
    page.title = "Sistema SIGE"
    page.window_width = 450
    page.window_height = 700

    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(e):
        # Limpiamos las vistas atuales para evitar duplicados en el historial
        page.views.clear()

        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))

        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))

        page.update()

        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("Error: Ruta no encontrada")])
            )

        page.update()

    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    # 1. Asignar los manejadores de eventos primero
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    if page.route == "/":
        route_change(None)
    else:
        page.go("/")

    page.on_route_change = route_change
    page.go("/")

if __name__ == "__main__":
    ft.app(target=start)