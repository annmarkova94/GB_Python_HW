# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

from copy import copy

def prime():
    my_list = []
    init_number = int(input('Enter an integer: '))
    number = copy(init_number)
    i = 2
    while i <= int(round(init_number/2 + 1, 0)):
        if number % i == 0:
            number /= i
            my_list.append(i)
            i = 1
        i += 1
    return my_list

print(prime())
