# 15.	Найти третью цифру числа или сообщить, что её нет

def get_number():
    while True:
        try:
            num = int(input())
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


print('Введите число a:')
a = get_number()


def thirdNumber(a):
    if (a % 1000//100) == 0:
        return f'Третьей цифры нет'
    else:
        return f'Третья цифра числа равна {(a % 1000//100)}'


print(thirdNumber(a))
