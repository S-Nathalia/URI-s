m, n = 0, 0
x, y = 0, 0

while(True):
    qs = int(input())
    if(not qs):
        break
    n, m = map(int, input().split(" "))

    while(qs != 0):
        x, y = map(int, input().split(" "))
        if(x < n and y > m):
            print("NO")
        elif(x > n and y > m):
            print("NE")
        elif(x < n and y < m):
            print("SO")
        elif(x > n and y < m):
            print("SE")
        else:
            print("divisa")
        qs -= 1
