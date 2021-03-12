import math

n1, n2, n3, n4 = map(float, input().split(" "))

def cal_media(n1, n2, n3, n4):
    media = 0.0
    media = (n1*2 + n2*3 + n3*4 + n4) / 10

    if(media >= 7):
        print("Media: %.1f" % media)
        print("Aluno aprovado.")

    elif(media < 5):
        print("Media: %.1f" % media)
        print("Aluno reprovado.")

    elif(5 <= media <= 6.9):
        print("Media: %.1f" % media)
        print("Aluno em exame.")
        nf = float(input())
        print("Nota do exame: %.1f" % nf)
        media = (media + nf) / 2
        if(media >= 5):
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")

        print("Media final: %.1f" % media)


cal_media(n1, n2, n3, n4)
