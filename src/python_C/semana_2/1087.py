x1, y1, x2, y2, x, y = 0, 0, 0, 0, 0, 0

while(True):
    x1, y1, x2, y2 = map(int, input().split(" "))
    if(x1 == 0):
        break

    # abs = valor absoluto i.e. 1 = abs(-1)
    x = abs(x2 - x1)
    y = abs(y2 - y1)

    # se x1 e x2 e y1 e y2 forem iguais, sera o mesmo ponto
    if(x1 == x2 and y1 == y2):
        print(0)

    # movimentos no eixo x fixo ou eixo y fixo exige apenas 1 movimento
    elif(x1 == x2 or y1 == y2):
        print(1)

    # movimentacao das diagonais
    elif(x == y):
        print(1)

    else:
        print(2)
