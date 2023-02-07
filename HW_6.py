import random
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# a = [int(input(f"Введите {i} точки А ")) for i in "xy"]
# b = [int(input(f"Введите {i} точки B ")) for i in "xy"]

# s = ((b[0]-a[0])**2+(b[1]-a[1])**2)**0.5
# print(round(s,3))

###

#45. Найти сумму чисел списка стоящих на нечетной позиции

# import random
# a = [random.randint(1, 21) for i in range (10)]
# print(a)
# select = [e for ind,e in enumerate(a) if ind%2==1]
# print(select)
# print(sum(select))

###
#46. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

# a = [random.randint(1, 6) for i in range (5)]
# mult = [a[ind]*a[-ind-1] for ind in range(len(a)//2+len(a)%2)]
# print(a)
# print(mult)

###

# 47.Сформировать список из N членов последовательности
# Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется)

n = int(input("Ввудите N: "))
list = [(-3)**i for i in range(n)]
print(list)