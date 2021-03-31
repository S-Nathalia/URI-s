while(True):
    n = int(input())
    if(n == 0):
        break
    s = 0
    p = 0
    error = [] # será responsável por armazenar os ids de subs incorretos
    subs = [] # analise de casos corretos
    for i in range(n):
        subs = list(map(str, input().split()))
        if(subs[2] == 'incorrect'):
            error.append(subs[0])
        if(subs[2] == 'correct'):
            s += 1 # quantidade de questoes corretas
            p += int(subs[1]) # soma o tempo da questao ao total do grupo
            n = error.count(subs[0]) # retorna qnt incorretas da qst correta atual
            p += n * 20 # 20 = penalidade correta
    print(s, p)
