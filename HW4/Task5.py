# Даны два файла, в каждом из которых находится запись многочленов
# Задача - сформировать файл, содержащий сумму многочленов

# path1 = r'C:\Users\annmark\YandexDisk\GB\8. Python\GB_Python_Homeworks\HW4\poly1.txt'
# with open(path1, 'r') as poly1:
#     for line in poly1:
#         print(line)

def sum_files(path1, path2, path3):
    with open(path1, 'r') as poly1, open(path2, 'r') as poly2, open(path3, 'w') as poly3:
        content1 = poly1.readlines()
        content2 = poly2.readlines()
        count_poly1 = 0
        count_poly2 = 0
        for line1 in content1:
            count_poly1 += 1
        for line2 in content2:
            count_poly2 += 1
        

        if count_poly1 != count_poly2:
            print('Files have different size')
        else:
            print('We are cool')
            num = 1
            for line1, line2 in zip(content1, content2):
                if line2[0:3] == ' - ':
                    poly3.write(line1[0:(len(line1) - 4 - num)] + line2)
                else:
                    poly3.write(line1[0:(len(line1) - 4 - num)] + ' + ' + line2)
                num = 0


path1 = r'C:\Users\annmark\YandexDisk\GB\8. Python\GB_Python_Homeworks\HW4\poly1.txt'
path2 = r'C:\Users\annmark\YandexDisk\GB\8. Python\GB_Python_Homeworks\HW4\poly2.txt'
path3 = r'C:\Users\annmark\YandexDisk\GB\8. Python\GB_Python_Homeworks\HW4\poly3.txt'
sum_files(path1, path2, path3)