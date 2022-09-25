# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def some_weird_function(x, y, z):
    # SHOW POSITIVE CASES
    # for x in range(2):
    #     for y in range(2):
    #         for z in range(2):
    #             if not (x or y or z) == (not x) and (not y) and (not z):
    #                 print(x, y, z, not (x or y or z), (not x) and (not y) and (not z))
    if not (x or y or z) == (not x) and (not y) and (not z):
        print('This is True')
    else:
        print('This is False')

some_weird_function(True, False, False)

# SHOW POSITIVE CASES
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x) and (not y) and (not z):
                print(x, y, z, not (x or y or z), (not x) and (not y) and (not z))
