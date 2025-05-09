import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View, colors
from flet.core import page
from flet.core.colors import Colors



def main(page: Page):
    page.title = "Exemplo de rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    ElevatedButton(text="Navegar", on_click=lambda _: page.go("/segunda")),
                ],
            )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda"), bgcolor=Colors.SECONDARY_CONTAINER),
                    ],
                )
            )

        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

ft.app(main)
