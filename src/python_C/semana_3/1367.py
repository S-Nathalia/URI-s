while(True):
    n = int(input())
    if(n == 0):
        break
    s = p = 0
    error = subs = []
    for i in range(n):
        subs = list(map(str, input().split()))
        if(subs[2] == 'incorrect'):
            error.append(subs[0])
        if(subs[2] == 'correct'):
            s += 1
            p += int(subs[1])
            n = error.count(subs[0])
            if(n != 0):
                p += n * 20
    print(s, p)
