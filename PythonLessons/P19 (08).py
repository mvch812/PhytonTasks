# 19.	Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

# x = -100
# y = 9


# def Chetvert(x, y):

#     if (x > 0):
#         if (y > 0):
#             return 1
#         else:
#             return 4
#     else:
#         if (y > 0):
#             return 2
#         else:
#             return 3


# print(f'Координата ({x},{y}) находится в {Chetvert(x, y)}-й четверти')


# 8.	Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

x = 0
y = 0


def Chetvert(x, y):
    if (y == 0 and x == 0):
        return f'Координата ({x},{y}) находится в месте пересечения осей координат X и Y'
    elif (x > 0 and y == 0) or (x < 0 and y == 0):
        return f'Координата ({x},{y}) находится на оси Y'
    elif (y > 0 and x == 0) or (y < 0 and x == 0):
        return f'Координата ({x},{y}) находится на оси X'
    elif (y > 0 and x > 0):
        return f'Координата ({x},{y}) находится в 1-й четверти'
    elif (y < 0 and x > 0):
        return f'Координата ({x},{y}) находится в 4-й четверти'
    elif (y < 0 and x < 0):
        return f'Координата ({x},{y}) находится в 3-й четверти'
    else:
        return f'Координата ({x},{y}) находится во 2-й четверти'


print(Chetvert(x, y))