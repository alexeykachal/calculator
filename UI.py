
import verification as v

def ordinary_number(number):
    '''
    Ввод простого числа
    '''
    input_data = f'Введите обычное число {number}: '
    return v.verify_float_number(input_data)

def complex_number(number):
    '''
    Ввод обычного числа
    '''
    input_x = f'Введите действительную часть числа {number}: '
    input_i = f'Введите мнимую часть числа {number}: '
    return v.verify_int_number(input_x), v.verify_int_number(input_i)

def sign_choice(sign):
    '''
    Ввод операции
    '''
    input_sign = f'Введите знак операции, выбрав из "+", "-", "/", "*", "**", "root" {sign}: '
    return v.verify_sign(input_sign)

def calc_choice(number):
    '''
    Выбор калькулятора
    '''
    number = f'Введите номер калькулятора: '
    return v.verify_calculator(number)

def calc_result(data,res):
    '''
    Вывод результата
    '''
    print(f'для этого набора данных {data} ответ будет {res}')
