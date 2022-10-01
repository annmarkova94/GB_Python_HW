# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

def f(amount):
    my_list = random.choices(range(10), k = amount)
    print(my_list)
    new_list = []
    if len(my_list) % 2 == 0:
        for i in range(int(amount/2)):
            new_list.append(my_list[i] * my_list[-i - 1])
    else:
        for i in range(int(amount/2) + 1):
            if i == int(amount/2):
                new_list.append(my_list[i])
            else:
                new_list.append(my_list[i] * my_list[-i - 1])

    return new_list

amount = int(input('Enter the list length: '))
print(f'Answer = {f(amount)}')
