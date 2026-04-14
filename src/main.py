import flet as ft
from controllers.UserController import AuthController
from controllers.TareaController import TareaController
from views.LoginView import LoginView
from views.dashboard import DashboardView

def main(page: ft.Page):
    # Instanciamos los controladores una sola vez
    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
        
        # caso de seguridad: si algo falla, mostrar texto de error
        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("Error:Ruta no encontrada o visita vacia")])
            )

        page.update()

    page.on_route_change = route_change
    # Forzamos la navegacion inicial
    page.go("/")

def main():
    # Ejecucion de la app
    ft.app(target=start)

if __name__ == "__main__":
    main()