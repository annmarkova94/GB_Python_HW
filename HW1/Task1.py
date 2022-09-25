# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

def weekday(number):
    if number == 6 or number ==7:
        print('Yes, this is a weekend day')
    elif number >=1 and number <=5:
        print('No, this is a working day')
    else:
        print('Error: the number is not in the range [1,7]')

weekday(int(input('Enter a number of a weekday and we will tell you if it is a weekend or a working day: ')))