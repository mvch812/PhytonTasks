# 2.	По двум заданным числам проверять является ли первое квадратом второго
print('Введите число a:')
а = float(input())
print('Введите число b:')
b = float(input())
print('Число a является квадратом числа b? Ответ:')
print(round(b*b, 2) == а)
