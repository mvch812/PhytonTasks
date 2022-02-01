# 11.Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.


import random
n = random.randint(1, 20)

print('Случайное число:', n)


def sequence(n):
    seq = [1]
    for i in range(1, n):
        seq.append(seq[i-1]*-3)
    return seq


print(sequence(n))
