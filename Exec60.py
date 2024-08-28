numeroI = 1
numeroF = 0
numero = int(input("Digite o número da tabuada: "))
while (numeroI>numeroF):
    numeroI = int(input("Digite o número inicial: "))
    numeroF = int(input("Digite o número final: "))
while numeroI<=numeroF:
    print(f"{numero} X {numeroI} = {numero*numeroI}")
    numeroI=numeroI+1