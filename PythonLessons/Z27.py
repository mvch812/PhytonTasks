# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

s = '233 44 556 2 2 13 3445 5 6 22 -21'


def MinMaxInString(s):
    l = list(map(int, s.split(' ')))
    min = l[0]
    max = l[0]
    for i in range(1, len(l)):
        if l[i] > max:
            max = l[i]
        else:
            if l[i] < min:
                min = l[i]
    return (min, max)


print(
    f'В строке чисел:{s} наибольшее число равно: {MinMaxInString(s)[1]}, а наименьшее: {MinMaxInString(s)[0]} ')
