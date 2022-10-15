# Вычислить число c заданной точностью d

from decimal import Decimal

def f_round():
    number = input('Enter a real number like "5.67: ')
    accuracy = input('Enter the required accuracy like "0.001": ')
    return Decimal(number).quantize(Decimal(accuracy))

print(f_round())
