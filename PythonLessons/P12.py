# 12.	Дано число из отрезка [100, 999]. Показать наибольшую цифру числа
import random
b = random.randint(100, 1000)
b1 = b//100
b2 = b % 100//10
b3 = b % 10
print(f'Случайное число:{b}')


def MaxNumber(k, b, c):

    if b > k and b > c:
        return (b)
    elif c > k and c > b:
        return (c)
    else:
        return (k)


print(f'Наибольшая цифра числа:{MaxNumber(b1, b2, b3)}')
