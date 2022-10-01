# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonach(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonach(n - 1) + fibonach(n - 2)


def fib_list(n):
    fib_list = []
    for i in range(-n, n + 1):
        if i < 0:
            fib_list.append(fibonach(-i) * (-1) ** ((i + 1) % 2))
        elif i == 0:
            fib_list.append(0)
        else:
            fib_list.append(fibonach(i))
    return fib_list


amount = int(input('Enter amount of numbers: '))
print(fib_list(amount))
