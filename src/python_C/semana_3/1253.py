q = int(input())

for i in range(q):
    texto = input()
    q = int(input())
    saida = ''
    for l in texto:
        ''' a função ord ja usa os indices de elementos da tabela ascii
        i.e. idx recebe o indice da letra pulada o numero de casas desejadas
        o menos é usado, porque apesar de a questão mencionar switches sempre
        para direita, as saídas do exemplo pulam para letras da esquerda '''
        idx = ord(l)-q

        if(idx < 65): # posicao 65 é onde começa o alfabeto na tabela ascii
            saida += chr(91 - (65 - idx)) # 91 = Z + 1, 65 = A; ou seja, o idx
                                          # q esteja dentro do intervalo de A-Z
        else:
            saida += chr(ord(l)-q) # caso contrario a posicao de l menos as casas
                                   # que se deve pular
    print(saida)
