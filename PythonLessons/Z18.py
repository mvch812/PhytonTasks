# 18.Реализовать алгоритм перемешивания списка.
import random

Numbers1 = [int(i)*random.randint(1, 100)
            for i in range(-10, 10)]  # случайный список
print(Numbers1)


Numbers1 = random.sample(Numbers1, len(Numbers1))
print(Numbers1)

