# 24.В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
#  Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


s = [1.1, 1.000000002, 3.1, 5, 10.01]


def get_count(number):  # функция определения количества знаков после запятой вещественного числа
    if number < 0.0001:
        number = number+0.1
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0


def delta(s):

    max = round(s[0]-int(s[0]), get_count(s[0]))
    min = round(s[0]-int(s[0]), get_count(s[0]))
    for i in range(1, len(s)):

        if round(s[i]-int(s[i]), get_count(s[i])) > max and get_count(s[i]) != 0:
            max = round(s[i]-int(s[i]), get_count(s[i]))
        else:
            if round(s[i]-int(s[i]), get_count(s[i])) < min and get_count(s[i]) != 0:
                min = round(s[i]-int(s[i]), get_count(s[i]))
        print(min, max)

    if get_count(max) >= get_count(min):
        return round(max-min, get_count(max))
    else:
        return round(max-min, get_count(min))


print(
    f'В заданном списке вещественных чисел: {s}, разница между максимальным и минимальным значением дробной части элементов равна: {delta(s)}')
