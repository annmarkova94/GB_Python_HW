# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

def sum_of_numbers(x):
    x_new = int(x * 10 ** len(str(x)))
    the_sum = 0
    for i in range(len(str(x_new))):
        the_sum += x_new % 10
        x_new = x_new // 10
    print(f'The sum is {the_sum}')

sum_of_numbers(float(input('Enter a number: ')))