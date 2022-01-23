# 17.	По двум заданным числам проверять является ли одно квадратом другого
def get_number():
    while True:
        try:
            num = int(input())
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


print('Введите число a:')
a = get_number()
print('Введите число b:')
b = get_number()


def SquareNumber(a, b):
    if a == b**2:
        print(f'число {a} является квадратом числа {b}')
    elif b == a**2:
        print(f'число {b} является квадратом числа {a}')
    else:
        print('Ни одно из чисел не является квадратом другого')


SquareNumber(a, b)
