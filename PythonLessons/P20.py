# 20.	Задать номер четверти, показать диапазоны для возможных координат
from P05 import MaxNumber

b = int(input())


def Range(b):
    if (b == 1):
        return f'Диапазон по Х (от 0 до {float.maxsize}), диапазон по Y (от 0 до {float.MaxNumber})'
    # elif (b == 2)
    # {
    #     return f"Диапазон по Х (от {double.MinValue} до 0), диапазон по Y (от 0 до {double.MaxValue})";
    # }
    # elif (b == 3)
    # {
    #     return f"Диапазон по Х (от {double.MinValue} до 0), диапазон по Y (от {double.MinValue} до 0)";
    # }
    # elif (b == 4)
    # {
    #     return f"Диапазон по Х (от 0 до {double.MaxValue}), диапазон по Y (от {double.MinValue} до 0)";
    # }
    else:
        return f'Номер четверти задан неверно!'


print(f'Диапазон возможных координат для {b} четверти: {Range(b)}')
