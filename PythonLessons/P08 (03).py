# 8.	Показать числа от -N до N
print('Введите число:')
b = int(input())
for i in range(0, b*2+1):
    j = -b+i
    print(j, end=" ")
