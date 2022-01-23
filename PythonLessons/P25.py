# 25.	Найти сумму чисел от 1 до А
print('Введите число A:')
a = int(input())


def Summ1ToA(a):
    return ((a + 1) * a) / 2


print(f'Сумма чисел от 1 до {a} равна: {Summ1ToA(a)}')
