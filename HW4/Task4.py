# Задана натуральная степень k
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена
# Pаписать в файл полученный многочлен не менее 3-х раз

import random

def func_generator(k):
    func = ""
    a = 0
    for i in range(k, -1, -1):
        koeff = random.randint(-10, 11)
        # print(f'{i}, koeff = {koeff}')
        if koeff > 0:
            if i == 0 and a == 0:
                func += f'{koeff}'
            elif i == 0:
                func += f' + {koeff}'
            elif a == 0:
                func += f'{koeff}*x^{i}'
            else:
                func += f' + {koeff}*x^{i}'
            a += 1
        if koeff < 0:
            if i == 0 and a == 0:
                func += f' - {-koeff}'
            elif i == 0:
                func += f' - {-koeff}'
            elif a == 0:
                func += f' - {-koeff}*x^{i}'
            else:
                func += f' - {-koeff}*x^{i}'
            a += 1
    return func

k = int(input('Enter an integer: '))
# print(func_generator(k))

with open(r'C:\Users\annmark\YandexDisk\GB\8. Python\GB_Python_Homeworks\HW4\HW4_Task4.txt', 'a') as data:
    data.write(func_generator(k)+'\n')
