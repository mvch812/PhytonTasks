# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
#  Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def negfib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return negfib(n+2)-negfib(n+1)


n = int(input('введите число: '))

list = [0]
for i in range(1, n+1):
    list.append(fib(i))
    list.insert(0, negfib(-i))
print(list)
