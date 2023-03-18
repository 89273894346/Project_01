def switch_it_up(number):
    number_dict = {
        0 : 'Zero', 1 : 'One', 2 : 'Two',
        3 : 'Three', 4 : 'Four', 5 : 'Five',
        6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine'
        }
    # number_dict.get(number, None)

    print(number_dict.get(number, None)) 

search = input('Введите цифру: ')
number = int(search)

switch_it_up(number)