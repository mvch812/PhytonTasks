# # 5.	Найти максимальное из трех чисел
# import random
# k = random.randint(1, 100)
# b = random.randint(1, 100)
# c = random.randint(1, 100)
# print(k, b, c)


# def MaxNumber(k, b, c):

#     if b > k and b > c:
#         return (b)
#     elif c > k and c > b:
#         return (c)
#     else:
#         return (k)


# print(f"максимальное из трех чисел:{MaxNumber(k, b, c)}")


# 2.	Найти максимальное из пяти чисел
import random
Numbers = []


def FillNumbers(Numbers):
    for i in range(5):
        Numbers.append(random.randint(1, 100))
    return Numbers


print(FillNumbers(Numbers))


def MaxNumber(Numbers):
    max = Numbers[0]
    for i in range(5):
        if Numbers[i] > max:
            max = Numbers[i]
    return max


print(
    f"Максимальное из случайных пяти чисел:{Numbers} равно: {MaxNumber(Numbers)}")
