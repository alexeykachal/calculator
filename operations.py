
x = 0
y = 0

def compile(ax, ay, bx, by):
    global x
    global y
    x = complex(ax,ay)
    y = complex(bx,by)

def ratio(a,b):
    global x
    global y
    x = float(a)
    y = float(b)

def sum():
    return x + y

def sub():
    return x - y

def mult():
    return x * y

def div():
    try:
        return x / y
    except ZeroDivisionError:
        print("произошло деление на ноль")



def degree():
    '''
    Первое число возводится в степень равную числу два
    '''
    return x ** y

def root():
    '''
    Первое число - число, из которого нужно извлечь корень. Второе число - корень какой степени извлекаем
    '''
    return x ** (1/y)