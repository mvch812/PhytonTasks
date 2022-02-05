# 23.Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

s = [2, 3, 4, 5, 6, 2, 3]

print(int(len(s)/2))


def multiplication(s):
    p = []
    if len(s) % 2 == 0:
        for i in range(int(len(s)/2)):
            p.append(s[i]*(s[-(i+1)]))
        return p
    else:
        for i in range(int((len(s)+1)/2)):
            p.append(s[i]*(s[-(i+1)]))
        return p


print(multiplication(s))
