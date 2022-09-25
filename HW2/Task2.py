# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

def factorials(N):
    list_of_factorials = [1]
    for i in range(2,N+1):
        list_of_factorials.append(list_of_factorials[i-2] * i)
    print(list_of_factorials)

factorials(int(input('Enter a number: ')))