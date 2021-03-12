time_fim = []
d1, d2 = 0, 0

dia1 = list(map(str, input().split(" ")))
time1 = list(map(int, input().split(" : ")))

dia2 = list(map(str, input().split(" ")))
time2 = list(map(int, input().split(" : ")))

d1 = int(dia1[1])
d2 = int(dia2[1])
d2 = d2 - d1

for i in range(len(time1)):
    time_fim.append(time2[i] - time1[i])

if(time_fim[2] < 0):
    time_fim[2] += 60
    time_fim[1] -= 1

if(time_fim[1] < 0):
    time_fim[1] += 60
    time_fim[0] -= 1

if(time_fim[0] < 0):
    time_fim[0] += 24
    d2 -= 1

print("%i dia(s)" % d2)
print("%i hora(s)" % time_fim[0])
print("%i minuto(s)" % time_fim[1])
print("%i segundo(s)" % time_fim[2])
