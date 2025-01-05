import flet as ft

from calculadora_de_horas.minha_jornada.src.main.services.calc_service import sum_hour, clean_cache, valid_hour, \
    get_hour


def main(page):
    def enter_pressed(e):
        if e.key == 'Enter':
            save(e)
    def save(e):
        if not valid_hour(enter_initial_hour.value):
            enter_initial_hour.error_text = "A hora deve estar no formato 00:00"
            page.update()
        if not valid_hour(enter_final_hour.value):
            enter_final_hour.error_text = "A hora deve estar no formato 00:00"

            page.update()
        else:
            total_hour.value = f'Horas trabalhadas: {sum_hour(enter_initial_hour.value, enter_final_hour.value)}'
            enter_initial_hour.error_text = None
            enter_final_hour.error_text = None
            enter_initial_hour.value = ''
            enter_final_hour.value = ''
            enter_initial_hour.focus()
            page.update()

    def clean(e):
        total_hour.value = f'Horas trabalhadas: 00:00'
        page.update()
        clean_cache()

    page.window.width = 500
    page.window.height = 350
    page.title = 'Calculadora de horas trabalhadas'
    btn_line = ft.Row()

    enter_initial_hour = ft.TextField(label='Digite o horário de entrada no formato 00:00', autofocus=True,
                                      border=ft.InputBorder.UNDERLINE)
    enter_final_hour = ft.TextField(label='Digite o horário de saída no formato 00:00', border=ft.InputBorder.UNDERLINE)
    total_hour = ft.Text(value=f'Horas trabalhadas: {get_hour()}')
    submit = ft.ElevatedButton(text='enviar', on_click=save)
    clean_calc = ft.ElevatedButton(text='Limpar Calculo', on_click=clean)
    enter_final_hour.width = 400
    enter_initial_hour.width = 400
    enter_initial_hour.error_text = None
    enter_final_hour.error_text = None
    btn_line.controls.append(submit)
    btn_line.controls.append(clean_calc)
    btn_line.spacing = 50
    page.on_keyboard_event = enter_pressed
    page.add(enter_initial_hour, enter_final_hour, total_hour, btn_line)


ft.app(target=main)
