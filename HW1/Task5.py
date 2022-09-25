# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def distatnce2D(pointA_x, pointA_y, pointB_x, pointB_y):
    distance = ((pointA_x-pointB_x)**2 + (pointA_y - pointB_y)**2)**(1/2)
    print(f'Distance is {round(distance, 3)}')

pointA_x = int(input('Point A, x coordinate: '))
pointA_y = int(input('Point A, y coordinate: '))
pointB_x = int(input('Point B, x coordinate: '))
pointB_y = int(input('Point B, y coordinate: '))

distatnce2D(pointA_x, pointA_y, pointB_x, pointB_y)
