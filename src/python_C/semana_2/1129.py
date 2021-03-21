A, B, C, D, E = 0, 0, 0, 0, 0

while(True):
    qs = int(input())

    if(not qs):
        break
    while (qs != 0):
        A, B, C, D, E = map(int, input().split(" "))
        if(A <= 127 and B > 127 and C > 127 and D > 127 and E > 127):
            print("A")
        elif(A > 127 and B <= 127 and C > 127 and D > 127 and E > 127):
            print("B")
        elif(A > 127 and B > 127 and C <= 127 and D > 127 and E > 127):
            print("C")
        elif(A > 127 and B > 127 and C > 127 and D <= 127 and E > 127):
            print("D")
        elif(A > 127 and B > 127 and C > 127 and D > 127 and E <= 127):
            print("E")
        else:
            print("*")
        qs -= 1
