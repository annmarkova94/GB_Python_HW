# Напишите программу, которая принимает на вход 2 числа
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]
# Найдите произведение элементов на указанных позициях(не индексах)


def some_function(pos_1, pos_2, N):
    result_list = list(range(-N, N+1))
    product = result_list[pos_1 - 1] * result_list[pos_2 - 1]
    print(f'Result list: {result_list}. The product of numbers on given positions = {product}')


pos_1 = int(input('Position one: '))
pos_2 = int(input('Position two: '))
N = int(input('Number of elements: '))
some_function(pos_1, pos_2, N)
