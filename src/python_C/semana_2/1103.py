while(True):
    try: #motivo do try: estava dando EOF Error como runtimerror no uri
        entrada = input()
        if(entrada == "0 0 0 0"):
            break

        min = []
        min = list(map(int, entrada.split(" ")))
        # horas transformadas em minutos
        min[0] *= 60
        min[2] *= 60
        # soma das horas com os min
        min[0] += min[1]
        min[2] += min[3]
        # se a hora de termino for menor que a hora de inicio, significa
        # que o dia virou
        if(min[2] < min[0]):
            # calcular o que falta para completar 24 horas
            # 24 horas possui 1440 minutos
            aux = 1440 - min[0]
            print(aux + min[2])
        else:
            print(min[2] - min[0])
    except:
        break
