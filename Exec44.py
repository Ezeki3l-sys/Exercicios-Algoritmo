inicio = int(input("Digite um número: "))
fim = inicio-1
while (fim<inicio):
    fim = int(input("Digite um número maior que o anterior: "))


while (inicio<fim):
    inicio = inicio + 1
    if (inicio==fim):
        break
    print (inicio)