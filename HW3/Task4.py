# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random as rnd

def f(amount):
    my_list = [round(x * rnd.random(), 2) for x in rnd.choices(range(10), k = amount)]
    print(f'The list: {my_list}')
    my_list_fract = [round(x % 1 * 100) for x in my_list]
    maximum = max(my_list_fract)
    minimum = min(my_list_fract)
    return maximum - minimum

amount = int(input('Enter amount of numbers: '))
print(f'The max and min fractions difference = {f(amount)}')