# 4.	По заданному номеру дня недели вывести его название
import random
а = random.randint(1, 7)
print(f'Номер дня недели:{а}')


def daysOfweek(num):
    days = ['понедельник', 'вторник', 'среда',
            'четверг', 'пятница', 'суббота', 'воскресенье']
    return days[num-1]


print(daysOfweek(а))