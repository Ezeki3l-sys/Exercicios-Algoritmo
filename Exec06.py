n1 = int(input("DIgite o 1° número: "))
n2 = int(input("DIgite o 2° número: "))
operador = input("Digite o operador entre + e - :")[0]

if (operador == "+"):
    resultado = n1 + n2
    print (f"O resultado é {resultado}")
elif (operador == "-"):
    resultado = n1 - n2
    print (f"O resultado é {resultado}")
else:
    print ("operador inválido.")
