#Вычислить число c заданной точностью d
import math
d = input()
lenght = d.split(".")[1]
print(round(math.pi, lenght))