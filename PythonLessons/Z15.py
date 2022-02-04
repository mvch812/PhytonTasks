# 15.	Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

print('Введите N:')
b = int(input())


def Nab(b):
    res = [1]
    for i in range(2, b+1):
        res.append(i*res[i-2])
    return res


print(Nab(b))
