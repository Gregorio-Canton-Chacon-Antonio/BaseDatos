import flet as ft
from controllers.UserController import AuthController
from controllers.TareaController import TareaController
from views.LoginView import LoginView
from views.dashboard import DashboardView

def start(page: ft.Page):
    page.title = "Sistema SIGE"
    page.window_width = 450
    page.window_height = 700

    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
        page.update()

    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Cargamos la vista inicial directamente
    page.views.append(LoginView(page, auth_ctrl))
    page.update()

def main():
    ft.run(main=start)

if __name__ == "__main__":
    main()
