a, b = 0, 0

while(True):
    try:
        a, b = map(int, input().split(" "))
        print(a ^ b)
    except:
        break
