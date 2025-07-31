#alunos =   [["Vitor"],[],[],[],[],[]],[["Maria"],[],[],[],[],[]],[["Felipe"],[],[],[],[],[]],[["Nicolas"],[],[],[],[],[]]
boletim= dict()
notas = []

for i in range(4):
    nome = input("Digite o nome do aluno: ").lower()
    if (boletim.get(nome)):
        pass
    else:
        notas = []
        for x in range(4):
            nota = float(input(f"Digite a {x+1}º nota: "))
            notas.append(nota)
        notas.append(sum(notas)/4)    

        boletim[nome]= notas

print(boletim)