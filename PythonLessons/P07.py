# 7.	Выяснить является ли число чётным
import random
m = random.randint(1, 100)
print('Случайное число:', m)


def EvenNum(m):
    return m % 2 == 0


print(f'Случайное число является четным?Ответ:{EvenNum(m)}')
