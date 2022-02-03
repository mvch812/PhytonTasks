# 14.	Подсчитать сумму цифр в вещественном числе.

import random
k = random.uniform(-100, 100)
m = str(k).replace('.', '', 1).replace('-', '', 1)
# print(f'Случайное число:{k}')


def summ(m):
    sum = 0
    for i in range(len(m)):
        sum += int(m[i])
    return sum


print(f'Сумма цифр случайного вещественного числа: {k} = {summ(m)}')
