# Задача 1.3.

import datetime
search = input('Введите номер месяца: ')
month_number = int(search)
if month_number >= 1 and month_number <= 12:
    if month_number in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month_number in [4, 6, 9, 11]:
        days = 30
    elif month_number == 2:
        days = 28    
    print('Вы ввели ', datetime.date(2023, month_number, 1).strftime('%B'), '. ', days, ' дней')
else:
    print('Такого месяца нет!')