# 13.	Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.

print('Введите строку 1:')
b = input()
print('Введите строку 2:')
z = input()


def CountInSTR(b, z):
    return b.count(z)


print(CountInSTR(b, z))
