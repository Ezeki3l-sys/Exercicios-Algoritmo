notas = []

n = 0
while (n<5):
    notas.insert(n, input("Digite a matéria e as notas do aluno: "))
    n=n+1
notas.append((int(notas[1]) + int(notas[2]) + int(notas[3]) + int(notas[4]))/4)
if (notas[5]>=7):
    print (f"Aprovado em {notas[0]}. ")
elif (notas[5]<7 and notas[5]>=5):
    print (f"Recuperação em {notas[0]}. ")
else:
    print (f"Reprovado em {notas[0]}. ")