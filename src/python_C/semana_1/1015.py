import math

def calcular_distancia(x1, y1, x2, y2):
    p1 = pow((x2 - x1), 2)
    p2 = pow((y2 - y1), 2)
    distancia = math.sqrt((p1 + p2))
    print(round(distancia, 4))

x1, y1 = map(float, input().split(" "))
x2, y2 = map(float, input().split(" "))

calcular_distancia(x1, y1, x2, y2)
