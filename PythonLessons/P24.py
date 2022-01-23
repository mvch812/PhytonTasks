# 24.	Найти кубы чисел от 1 до N
print('Введите число N:')
n = int(input())


def cubeNumber(n):
    print(f"| число | куб числа |")
    print(f"_________________________")
    q = 0
    for i in range(1, n+1):
        q = i**3
        print("|%7d|%16d|" % (i, q))  # https://pythoner.name/formatted-output


cubeNumber(n)