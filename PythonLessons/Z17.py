# 17.Задать список из N элементов, заполненных числами из [-N, N].
#  Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
#  в одной строке одно число

print('Введите N:')
n = int(input())

numbers = [i for i in range(-n, n+1)]
print(numbers)

m = 'Z17-1.txt'


def Posicion(numbers, path):
    with open(path, 'r') as data:
        positionList = [int(i) for i in data if int(i) <= (len(numbers)-1)]
        return positionList


print(Posicion(numbers, m))


def multiplication(listNumbers, listPosition):
    p = 1
    for i in listPosition:
        p *= listNumbers[i]
    return p


if Posicion(numbers, m) == []:
    print(
        f'В текстовом файле указаны позиции, которые отсутствуют в заданном списке [-N, N], произведение посчитать невозможно')
else:
    print(
        f'Произведение элементов на указанных в текстовом файле позициях равно: {multiplication(numbers, Posicion(numbers, m))}')
