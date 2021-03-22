a, b = 0, 0

while(True):
    try:
        a, b = map(int, input().split(" "))
        # XOR em python é feito pelo operador ^
        print(a ^ b)
    except:
        break
