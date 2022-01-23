# 11.	Показать вторую цифру трёхзначного числа


def get_number():
    while True:
        try:
            num = int(input("Введите трехзначное число: "))
            if num > 99 and num < 1000:
                return num
            else:
                print("Вы ввели не трехзначное число. Повторите ввод")
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


print(f'Вторая цифра введенного числа:{get_number()%100//10}')
