from calculadora_de_horas.minha_jornada.src.main.gui import calculator_gui
from calculadora_de_horas.minha_jornada.src.main.services.calc_service import sum_hour, clean_cache


def execute():
    clean_cache()
    print(sum_hour('23:30', '03:10'))



if __name__ == '__main__':
    # execute()
    calculator_gui