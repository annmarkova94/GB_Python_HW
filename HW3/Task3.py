# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

def binarize(number):
    number_binarized = 0
    list_of_digits = []
    while number > 0:
        list_of_digits.append(number % 2)
        number //= 2
    for i in range(len(list_of_digits)):
        number_binarized += list_of_digits[i] * 10 ** i
    return number_binarized

number = int(input('Enter your number: '))
print(binarize(number))