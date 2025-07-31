numero = int(input("Dgite um número > 0: "))
contador = numero-1
while (contador!=0):
    numero = numero*contador
    contador = contador - 1
print (f"O resultado é {numero}.")