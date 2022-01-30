# 4.	Показать первую цифру дробной части числа
import random
import math
n = random.uniform(-100, 100)


def FirstNum(n):
    return math.floor(abs(n)*10 % 10)


print(f'Первая цифра дробной части случайного числа {n} = {FirstNum (n)}')
