# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

import random


def unique(N):
    if N < 1:
        return "Error, the number must be positive"
    my_list = []
    unique_list = []
    for i in range(N):
        my_list.append(random.randint(1, 10))

    for item in my_list:
        if my_list.count(item) == 1:
            unique_list.append(item)
    
    return my_list, unique_list


N = int(input('Enter an integer: '))
print(unique(N))
