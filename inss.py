from cProfile import label
from optparse import Option

import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View, colors



from flet.core import page
from flet.core.colors import Colors
from flet.core.dropdown import Option

# ft.image(src="")
def main(page: ft.Page):
    page.title = "Exemplo de rotas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Aposentadoria"), bgcolor=Colors.WHITE),
                    ft.Image(src="INSS.jpg", width=350),
                    ElevatedButton(text="Simular", width=350, on_click=lambda _: page.go("/segunda")),
                    ElevatedButton(text="Regras", width=350, on_click=lambda _: page.go("/terceira")),
                ],
                bgcolor=Colors.BLUE
            )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Simulação da Aposentadoria"), bgcolor=Colors.WHITE),
                        input_idade_atual,
                        input_genero,
                        input_contribuicao,
                        input_salario,
                        input_categoria,
                        ElevatedButton(text="Enviar", on_click=lambda _: page.go("/quarta")),

                    ],
                    bgcolor=Colors.BLUE
                )
            )
        if page.route == "/terceira":
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text("Regras da Aposentadoria"), bgcolor=Colors.WHITE),
                        Text(value=f'APOSENTADORIA POR IDADE:\n'
                                   f'Homens: 65 anos de idade e pelo menos 15 anos de contribuição.\n'
                                   f'Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\n\n'
                                   f'APOSENTADORIA POR TEMPO DE CONTRIBUIÇÃO:\n'
                                   f'Homens: 35 anos de contribuição.\n'
                                   f'Mulheres: 30 anos de contribuição.\n\n'
                                   f'VALOR ESTIMADO DO BENEFÍCIO:\n'
                                   f'O valor da aposentadoria será uma média de 60%\n'
                                   f'da média salarial informada, acrescido de 2% por ano que exceder o tempo mínimo\n'
                                   f'de contribuição'),
                    ],
                    bgcolor=Colors.BLUE,
                ),
            )

        if page.route == "/quarta":
            page.views.append(
                View(
                    "/quarta",
                    [
                        AppBar(title=Text("Resultado da Aposentadoria"), bgcolor=Colors.WHITE),
                        ElevatedButton(text="Fazer de novo", on_click=lambda _: page.go("/segunda")),
                        ElevatedButton(text="Regras", on_click=lambda _: page.go("/terceira")),
                    ],
                    bgcolor=Colors.BLUE
                )
            )
        page.update()




    input_idade_atual = ft.TextField(label="Digite sua idade", border_color=Colors.WHITE, color=Colors.WHITE)
    input_contribuicao = ft.TextField(label="tempo de contribuição", border_color=Colors.WHITE, color=Colors.WHITE)
    input_salario = ft.TextField(label="média salarial dos últimos 5 anos", border_color=Colors.WHITE, color=Colors.WHITE)


    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    input_genero = ft.Dropdown(
        label="Gênero",
        options=[Option(key="Mas", text="Masculino"), Option(key="Fem", text="Feminino")],
        width=350, border_color=Colors.WHITE, color=Colors.WHITE
    )
    input_categoria = ft.Dropdown(
        label="Categoria da Aposentadoria",
        options=[Option(key="id", text="Por idade"), Option(key="Con", text="Por contribuição")],
        width=350, border_color=Colors.WHITE, color=Colors.WHITE
    )
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

ft.app(main)

