
# 15.	Дано число. Проверить кратно ли оно 7 и 23

import random
m = random.randint(1, 100)

print(f'Случайное число:{m}')
print(f'Число {m} кратно 7 и 23? Ответ:{m % 7 == 0 and m % 23==0}')