# 16.Задать список из n чисел последовательности (1+(1/n))^n и вывести на экран их сумму

print('Введите N:')
n = int(input())


def f(n):
    res = []
    for i in range(1, n+1):
        res.append((1+(1/i))**i)
    return res


print(f(n))


def fx(x):  # способ №2
    return (1+(1/x))**x


result = [fx(m) for m in range(1, n+1)]


def summa(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum


print(result)
print(sum(result))
print(summa(f(n)))
