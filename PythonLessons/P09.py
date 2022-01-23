# 9.	Показать четные числа от 1 до N
print('Введите число:')
b = int(input())


def Numbers1toN(b):
    for i in range(2, b+1, 2):
        print(i, end=" ")


Numbers1toN(b)
