import flet as ft

def main(page: ft.Page,):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

     # Definição de funções
    def somar(e):
        soma = int(input_numero1.value) + int(input_numero2.value)
        txt_resultado.value = f'Resultado = {soma}'
        page.update()

    def subtrair(e):
        subtrair = int(input_numero1.value) - int(input_numero2.value)
        txt_resultado.value = f'Resultado = {subtrair}'
        page.update()

    def dividir(e):
        dividir = int(input_numero1.value) / int(input_numero2.value)
        txt_resultado.value = f'Resultado = {dividir}'
        page.update()

    def multiplicar(e):
        multiplicar = int(input_numero1.value) * int(input_numero2.value)
        txt_resultado.value = f'Resultado = {multiplicar}'
        page.update()


    # Criação de componentes
    input_numero1 = ft.TextField(label="Número", col=4)
    input_numero2 = ft.TextField(label="Número", col=4)


    btn_somar = ft.FilledButton(
        text="Somar",
        width=page.window.width,
        on_click=somar)

    btn_multiplicar = ft.FilledButton(
        text="Multiplicar",
        width=page.window.width,
        on_click=multiplicar,)

    btn_dividir = ft.FilledButton(
        text="Dividir",
        width=page.window.width,
        on_click=dividir,)

    btn_subtrair = ft.FilledButton(
        text="Subtrair",
        width=page.window.width,
        on_click=subtrair,)


    txt_resultado = ft.Text(value="")


# Construir o layout
    page.add(
       ft.Column(
           [
               input_numero1,
               input_numero2,
               btn_somar,
               btn_subtrair,
               btn_dividir,
               btn_multiplicar,
               txt_resultado,
           ]
       )
    )

ft.app(main)

