# 12.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import random
n = random.randint(1, 20)


def dict(n):
    diction = {}
    for i in range(1, n):
        diction[i] = 3*i+1
    return diction


print(dict(n))
