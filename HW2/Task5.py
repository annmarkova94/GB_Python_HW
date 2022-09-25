#  Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random

import random


def shuffle_the_list(list_len):
    our_list = list(range(10))
    for i in range(100):
        x = random.randint(0, list_len-1)
        y = random.randint(0, list_len-1)
        helping = our_list[x]
        our_list[x] = our_list[y]
        our_list[y] = helping
    print(our_list)


shuffle_the_list(int(input('Enter the list length: ')))
