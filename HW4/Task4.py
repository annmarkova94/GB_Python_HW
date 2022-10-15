# Задана натуральная степень k
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена
# Pаписать в файл полученный многочлен не менее 3-х раз

import random

def func_generator(k):
    func = ""
    for i in range(0, k):
        koeff = random.randint(0, 11)
        # print(f'{i}, koeff = {koeff}')
        if koeff != 0:
            if i == 0:
                func = f'{koeff}' + func
            else:
                func = f'{koeff}*x^{i} + ' + func  
    return func

k = int(input('Enter an integer: '))

with open(r'C:\Users\annmark\YandexDisk\GB\8. Python\GB_Python_Homeworks\HW4\HW4_Task4.txt', 'a') as data:
    data.write(func_generator(k)+'\n')
