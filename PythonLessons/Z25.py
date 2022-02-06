# 25.Написать программу преобразования десятичного числа в двоичное

n = int(input('введите число для преобразования в двоичное: '))


def decimalToBinary(n):
    return bin(n).replace("0b", "")


print(f'Ответ: {decimalToBinary(n)}')
