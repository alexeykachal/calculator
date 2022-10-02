
def verify_int_number(number):
    '''
    Проверка является ли число целым
    '''
    while True:
        try:
            return int(input(number))
        except ValueError:
            print("Введено не целое число")

def verify_float_number(number):
    '''
    Проверка является ли число целым
    '''
    while True:
        try:
            return float(input(number))
        except ValueError:
            print("Введено не дробное число")

def verify_sign(sign):
    '''
    Проверка знака
    '''
    while True:
        try:
            s = input(sign)
            if s == "+" or s == "-" or s == "*" or s == "/" or s == "**" or s == "root":
                return s
            else:
                print("Введите корректный знак действия")
        except ValueError:
            print('')

def verify_calculator(choice):
    '''
    Проверка выбора калькулятора - 1 - обычные числа, 2 - комплексные числа
    '''
    while True:
        try:
            calc_choice = int(input(choice))
            if calc_choice == 1 or calc_choice == 2:
                return calc_choice
            else:
                print("Нужно выбрать один или два")
        except ValueError:
            print('Вы ввели не число')