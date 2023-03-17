# Задача 2.2. 

def quarter_of(month):
        Q = mont_numer / 3
        if Q <= 1:
            Q_ = 'первого'
        elif 1 < Q <= 2:
            Q_ = 'второго'
        elif 2 < Q <= 3:
            Q_ = 'третьего'
        else:
            Q_ = 'четвертого'
        return Q_

search = input('Введите номер месяца: ')
mont_numer = int(search)

if mont_numer >= 1 and mont_numer <= 12:
    print('Месяц ', mont_numer, ' является частью ', quarter_of(mont_numer), ' квартала.')
else:
    print('Такого месяца нет!')