m, n = 0, 0
x, y = 0, 0

while(True):
    qs = int(input())
    if(qs == 0):
        break
    n, m = map(int, input().split(" "))

    while(qs != 0):
        x, y = map(int, input().split(" "))

        if (x == n or y == m):
            print("divisa")
        elif (x < n): # x na esquerda do ponto
            if (y > m): # y acima do ponto
                print("NO") #Noroeste
            else: # y abaixo do ponto
                print("SO") #Sudoeste
        else: # x na direita do ponto
            if (y < m): # y abaixo do ponto
                print("SE") #Sudeste
            else: # y acima da ponto
                print("NE") #Nordeste
        qs -= 1
