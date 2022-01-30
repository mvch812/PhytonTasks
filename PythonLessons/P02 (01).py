# 2.	По двум заданным числам проверять является ли первое квадратом второго
# print('Введите число a:')
# а = float(input())
# print('Введите число b:')
# b = float(input())
# print('Число a является квадратом числа b? Ответ:')
# print(round(b*b, 2) == а)

# 1.	По двум заданным числам проверить является ли одно квадратом второго

print('Введите число a:')
a = float(input())
print('Введите число b:')
b = float(input())


def square_numbers(a, b):
    if round(b*b, 2) == a:
        return f'Число a является квадратом числа b'
    elif round(a*a, 2) == b:
        return f'Число b является квадратом числа a'
    else:
        return f'Ни одно из чисел не является квадратом второго'


print(square_numbers(a, b))
