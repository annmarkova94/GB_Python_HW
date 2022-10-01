# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах)

import random

def f(amount):
    my_list = random.choices(range(10), k = amount)
    print(f'The random list is: {my_list}')
    summa = 0
    for i in range(int(amount/2) + 1):
        summa += my_list[i*2]
    return summa

amount = int(input('Enter amount of numbers to generate a random list: '))
print(f'Sum of numbers on odd positions = {f(amount)}')