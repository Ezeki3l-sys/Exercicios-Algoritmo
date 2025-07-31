numeros = []

for n in range (0,5):
    numeros.append(int(input("Digite um valor: ")))

numeros.sort ()

print (f"O maior número é o {numeros[-1]}.")