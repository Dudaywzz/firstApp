import flet as ft

def main(page: ft.Page):
    # Configuração da página
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

     # Definição de funções
    def mostrar_par_ou_impar(e):
        try:
            num1 = int(input_numero.value)
            par_impar = num1 % 2
            if par_impar == 0:
                txt_resultado.value = "Par"
            else:
                txt_resultado.value = "Impar"
            page.update()
        except ValueError:
            txt_resultado.value = "Digite um valor inteiro"
            page.update()

    # Criação de componentes
    input_numero = ft.TextField(label="Número", hint_text="Digite um número")
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=mostrar_par_ou_impar,)
    txt_resultado = ft.Text(value="")

             # Construir o layout
    page.add(
       ft.Column(
           [
               input_numero,
               btn_enviar,
               txt_resultado,
           ]
       )
    )

ft.app(main)