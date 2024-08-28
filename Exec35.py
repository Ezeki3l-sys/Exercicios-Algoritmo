metrosq = int(input("Digite a quantidade de metros: "))
tinta = 54
preco_tinta = 80
contador = 0

if (metrosq <= tinta):
    print (f"Você precisa de 1 tinta e custará 80 reais. ")
else:
    while (metrosq > 0):
        metrosq = metrosq - tinta
        contador = contador + 1

    preco_tinta = preco_tinta * contador
    print (f"Você precisa de {tinta} latas de tinta e custará {preco_tinta} reais.")