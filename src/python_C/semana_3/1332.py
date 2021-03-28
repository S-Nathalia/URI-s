n = int(input())

for i in range(n):
    n2 = input()
    if(len(n2) == 5):
        print(3)
    else:
        if(n2[0] == 'o' and n2[1] == 'n'):
            print(1)
        elif(n2[0] == 'o' and n2[2] == 'e'):
            print(1)
        elif(n2[1] == 'n' and n2[2] == 'e'):
            print(1)
        else:
            print(2)
