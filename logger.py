
from datetime import datetime as dt

def logger(data, result):
    """
    Дневник операций
    """

    time = dt.now().strftime('%d.%m.%Y - %H:%M')
    with open('log.txt', 'a', encoding = 'UTF-8') as file:
        file.write(f'{time}: {data} = {result}\n')