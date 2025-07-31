numero = 1001
while (numero>=1000):
    numero = int(input("Digite um número menor que 1000: "))

    centenas = numero / 100
    dezenas = numero / 10
    unidade = numero%10

    print(f"A quantidade de centenas é {centenas}\n A quantidade de dezenas é {dezenas}\n A quantidade de unidades é {unidade}")