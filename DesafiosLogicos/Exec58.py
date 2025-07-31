tipo = str(input("A-álcool: 3.90 por litro, G-gasolina: 5,50 por litro: "))
litros = float(input("Quantos litros irá colocar? "))
if (tipo == "A"):
    if(litros<=20):
        preco = 3.90*litros*1.03
    else:
        preco = 3.90*litros*1.05
elif (tipo == "G"):
    if(litros<=20):
        preco = 5.50*litros*1.04
    else:
        preco = 5.50*litros*1.06
print(f"O preço do abastecimento será R${preco}")