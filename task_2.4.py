# Задача 2.4.


# Пункт A.
def remove_exclamation_marks(s):
    _s = s.replace('!', '')
    print(_s)

foo = str("Oh, no!!!")
remove_exclamation_marks(foo)   

# Пункт B.

def remove_last_em(s):
    s_lst = list(s)
    a = s_lst[len(s) - 1]

    if a == '!':
        s_str = ''
        i = 0
        while i < (len(s) - 1):
            s_str += s_lst[i]
            i = i + 1
    else:
        s_str = ''
        i = 0
        while i < (len(s)):
            s_str += s_lst[i]
            i = i + 1
    print(s_str)

s = str("!Hi")
remove_last_em(s)

# Пункт С. 

def remove_word_with_one_em(s):
    s_str = s.split(' ')
    for el in s_str:
        el_str1 = str(el)
        el_lst = list(el_str1)
        a = el_lst[len(el_str1) - 1]
        b = el_lst[len(el_str1) - 2]
        c = el_lst[0]
        if el_str1.count('!') == 1:
            continue
        if el_str1.count('!') != 1:
            el_str2 = ''
            i = 0
            while i < (len(el_str1)):
                el_str2 = el_str2 + el_lst[i]
                i = i + 1
        print(el_str2)

_s_ = str("Hi! !Hi! Hi!")
remove_word_with_one_em(_s_) 