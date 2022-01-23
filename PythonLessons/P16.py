# 16.	Дано число обозначающее день недели. Выяснить является номер дня недели выходным
# print('Введите число дня недели:')
# b = int(input())
def get_number():
    while True:
        try:
            num = int(input("Введите число дня недели: "))
            if num > 0 and num < 8:
                return num
            else:
                print("Такого дня недели не существует")
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


b = get_number()


def Weekend(b):
    return b == 6 or b == 7


print(f'Введенный номер дня недели выходной? Ответ:{Weekend(b)}')
