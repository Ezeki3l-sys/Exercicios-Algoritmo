n1 = int(input("Digite um número: "))
operador = str(input("DIgite o operador: "))[0]
n2 = int(input("Digite um número: "))


if (operador == "+"):
    print (n1+n2)
elif (operador == "-"):
    print (n1-n2)
elif (operador == "*"):
    print (n1*n2)
elif (operador == "/"):
    if (n2 != 0):
        print (n1/n2)
    else:
        print ("Impossível dividir por 0.")
    