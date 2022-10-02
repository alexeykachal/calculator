import logger as logs
import UI as ui
import operations as op


def button_click():
    '''
    Запрос данных пользователя
    '''
    name = ui.calc_choice("")
    if name == 1:
        first_num = ui.ordinary_number(1)
        sign = ui.sign_choice("")
        second_num = ui.ordinary_number(2)
        op.ratio(first_num, second_num)
    elif name == 2:
        first_num, first_mn = ui.complex_number(1)
        sign = ui.sign_choice("")
        second_num, second_mn = ui.complex_number(2)
        op.compile(first_num, first_mn, second_num, second_mn)

    if sign == "+":
        result = op.sum()
    if sign == "-":
        result = op.sub()
    if sign == "*":
        result = op.mult()
    if sign == "/":
        result = op.div()
    if sign == "**":
        result = op.degree()
    if sign == "root":
        result = op.root()
    if name == 1:
        if not ZeroDivisionError:
            result == round(result,10)
        else:
            result = "Делить на ноль нельзя!"




    data_log = str(op.x) + " " + sign + " " + str(op.y)
    ui.calc_result(data_log, result)
    logs.logger(data_log, result)