# ##-----------------------task1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
#~~~~~~~~~~~~~~~~~~~~~
# a = (input("Введите a= "))
# sum = 0
# for i in a:
#     if i.isdigit():
#         sum = sum + int(i)
# print('Сумма цифр', sum)
#~~~~~~~~~~~~~~~~~~~~~

# ##-----------------------task2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#~~~~~~~~~~~~~~~~~~~~~
# N = int(input("Введите N= "))
# List = []
# a = 1
# for i in range(1,N+1):
#     a=a*i
#     List.append(a)
# print(list)
#~~~~~~~~~~~~~~~~~~~~~

# ##-----------------------task3
# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#         Сумма 9.06
#~~~~~~~~~~~~~~~~~~~~~
# N = int(input("Введите N= "))
# List = []
# x = 0
# summ = 0
# for i in range(1,N+1):
#     x=((1+(1/i))**i)
#     summ+=x
#     List.append(x)
# print(List)
# print(round(summ,3))
#~~~~~~~~~~~~~~~~~~~~~

# ##-----------------------task4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.
#~~~~~~~~~~~~~~~~~~~~~
N = int(input("Введите N= "))
list = []
for i in range(1,N+1):
    list.append(i)
print(list)

file = open("file.txt", "r")
a=1
for e in file:
    a=list[int(e)]*list[(int(e)+1)]
    print(a)