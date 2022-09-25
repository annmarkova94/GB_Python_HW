# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def plane_number(x, y):
    if x > 0 and y > 0:
        print('1st plane')
    elif x < 0 and y > 0:
        print('2nd plane')
    elif x < 0 and y < 0:
        print('3rd plane')
    elif x > 0 and y < 0:
        print('4th plane')
    else:
        print('Error')

plane_number(int(input('X: ')), int(input('Y: ')))