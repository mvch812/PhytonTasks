# 21.	Программа проверяет пятизначное число на палиндромом.

def get_number():
    while True:
        try:
            num = int(input("Введите пятизначное число: "))
            if num > 9999 and num < 100000:
                return num
            else:
                print("Вы ввели не пятизначное число. Повторите ввод")
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


n = get_number()


def Polindrom(n):
    return (((n // 10000) == n % 10) and ((n // 1000 % 10) == (n // 10 % 10)))


print(f'Введенное число полиндром? Ответ: {Polindrom(n)}')
