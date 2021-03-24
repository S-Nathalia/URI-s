a, b, c, d = 0, 0, 0, 0
inicio, fim, aux = 0, 0, 0

while(True):
    a, b, c, d = map(int, input().split(" "))
    if(a == 0 and b == 0 and c == 0 and d == 0):
        break

    # horas transformadas em minutos
    inicio = (a*60) + b
    fim = (c*60) + d
    # se a hora de termino for menor que a hora de inicio, significa
    # que o dia virou
    if(fim < inicio):
        # calcular o que falta para completar 24 horas
        # 24 horas possui 1440 minutos
        inicio = 1440 - inicio
        print(inicio + fim)
    else:
        print(fim - inicio)
