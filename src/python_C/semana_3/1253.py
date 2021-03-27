q = int(input())

for i in range(q):
    texto = input()
    q = int(input())
    saida = ''
    for l in texto:
        idx = ord(l)-q

        if(idx < 65):
            saida += chr(91 - (65 - idx))
        else:
            saida += chr(ord(l)-q)
    print(saida)
