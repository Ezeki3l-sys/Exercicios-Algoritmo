pares = 0
impares = 0
for n in range (1,11):
    numero = int(input("Digite um número: "))
    if (numero%2==0):
        pares = pares + 1
    else:
        impares = impares + 1
print (f"Impares: {impares}\nPares: {pares}")