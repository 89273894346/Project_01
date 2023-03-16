# Пункт A.
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random
import datetime
my_favorite_songs_random = random.sample(my_favorite_songs, 3)

time = round(float(my_favorite_songs_random[0][1] + my_favorite_songs_random[1][1]) * 100 / 100, 2)

time_lst = str(time).split('.')

if int(time_lst[1]) >= 60:
    time_lst[1] = int(time_lst[1]) - 60
    time_lst[0] = int(time_lst[0]) + 1

time_2 = my_favorite_songs_random[2][1]
time_2_lst = str(time_2).split('.')

time_total = [int(time_lst[0]) + int(time_2_lst[0]), int(time_lst[1]) + int(time_2_lst[1])]

if time_total[1] > 60:
    time_total[1] -= 60
    time_total[0] += 1
    
print('Три песни звучат ', datetime.time(minute= time_total[0], second= time_total[1]).strftime('%M:%S'), ' минут')

#  Пункт B. 
my_favorite_songs_dict = {
     'Waste a Moment': 3.03,
     'New Salvation': 4.02,
     'Staying\' Alive': 3.40,
     'Out of Touch': 3.03,
     'A Sorta Fairytale': 5.28,
     'Easy': 4.15,
     'Beautiful Day': 4.04,
     'Nowhere to Run': 2.58,
     'In This World': 4.02,
}
import random
import datetime
my_favorite_songs_dict_random_lst = list(my_favorite_songs_dict)
my_favorite_songs_dict_random = random.sample(my_favorite_songs_dict_random_lst, 3)

time_dict_1 = my_favorite_songs_dict[str(my_favorite_songs_dict_random[0])]

time_dict_2 = my_favorite_songs_dict[str(my_favorite_songs_dict_random[1])]

time_dict = round(float(time_dict_1 + time_dict_2) * 100 / 100, 2)

time_dict_lst = str(time_dict).split('.')

if int(time_dict_lst[1]) >= 60:
    time_dict_lst[1] = int(time_dict_lst[1]) - 60
    time_dict_lst[0] = int(time_dict_lst[0]) + 1

time_dict_3 = my_favorite_songs_dict[str(my_favorite_songs_dict_random[2])]

time_dict_3_lst = str(time_dict_3).split('.')

time_dict_total = [int(time_dict_lst[0]) + int(time_dict_3_lst[0]), int(time_dict_lst[1]) + int(time_dict_3_lst[1])]

if time_dict_total[1] > 60:
    time_dict_total[1] -= 60
    time_dict_total[0] += 1
    
print('Три песни звучат ', datetime.time(minute= time_dict_total[0], second= time_dict_total[1]).strftime('%M:%S'), ' минут')    