numero = int(input("Digite um número: "))
primo = True
contador = numero-1

while (contador>1):
    if (numero%contador==0):
        primo = False
    contador=contador-1

if (primo==True):
    print (f"{numero} é primo.")
else:
    print (f"{numero} não é primo.")