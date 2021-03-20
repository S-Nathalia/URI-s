list = list(map(int, input().split(" ")))
str = []

for i in range(len(list)):
    str.append(list[i])

def bubble(list):
    maior = 0
    for i in range(len(list)-1):
        for k in range(len(list)-1):
            if(list[k] > list[k+1]):
                maior = list[k]
                list[k] = list[k+1]
                list[k+1] = maior
    return list

list = bubble(list)

for i in range(len(list)):
    print(list[i])
print()
for i in range(len(str)):
    print(str[i])
