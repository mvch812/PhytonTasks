# 5.	Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
p = 450


def multiplicity(p):
    return (p % 5 == 0 and p % 10 == 0 or p % 15 == 0) and p % 30 != 0


print(multiplicity(p))
