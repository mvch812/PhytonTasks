# 3.	Даны два числа. Показать большее и меньшее число
import random

а = random.randint(1, 100)
print('Случайное число a:')
print(а)
b = random.randint(1, 100)
print('Случайное число b:')
print(b)
if а > b:
    print('число a - большее, b - меньшее')
else:
    print('число b - большее, a - меньшее')

а = random.randint(1, 100)
