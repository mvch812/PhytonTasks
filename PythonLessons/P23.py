# 23.	Показать таблицу квадратов чисел от 1 до N
print('Введите число N:')
n = int(input())


def quadr(n):
    print(f"| число | квадрат числа |")
    print(f"_________________________")
    q = 0
    for i in range(1, n+1):
        q = i**2
        print("|%7d|%16d|" % (i, q))  # https://pythoner.name/formatted-output


quadr(n)
