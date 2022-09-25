# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму

def some_function(N):
    result_list = []
    for i in range(1, N + 1):
        result_list.append(round((1 + 1/i) ** i))
    print(f'Result list: {result_list}, the sum of its elements = {sum(result_list)}')


some_function(int(input('Enter a number: ')))
