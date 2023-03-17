# Задача 2.1.

def minimum(arr):
    i = 0
    _min = arr[i]
    while i < len(arr) - 1:
        if _min > arr[i + 1]:
            _min = arr[i + 1]
        i = i + 1
    return _min

arr_lst = [-52, 56, 30, 29, -54, 0, -110, 50]

def maximum(arr):
    i = 0
    _max = arr[i]
    while i < len(arr) - 1:
        if _max < arr[i + 1]:
            _max = arr[i + 1]
        i = i + 1
    return _max

arr_lst_2 = [4, 6, 2, 1, 9, 63, -134, 566, 50]

print('min = ', minimum(arr_lst), ', max = ', maximum(arr_lst_2))