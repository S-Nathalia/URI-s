str = "0 0 0 0"
min = []
aux = 0
aux2 = 0

while(True):
    entrada = input()
    if(entrada == str):
        break

    min = list(map(int, entrada.split(" ")))
    # horas transformadas em min
    min[0] = min[0] * 60
    min[2] = min[2] * 60
    # soma das horas com os min
    min[0] += min[1]
    min[2] += min[3]
    # se a hora de termino for menor que a hora de inicio, significa
    # que o dia virou
    if(min[2] < min[0]):
        # calcular o que falta para completar 24 horas
        # 24 horas possui 1440 min
        aux = 1440 - min[0]
        print(aux + min[2])
    else:
        print(min[2] - min[0])
