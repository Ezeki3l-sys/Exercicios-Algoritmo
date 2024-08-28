divisivel = ""
numero = int(input("DIgite um número: "))
if (numero % 5 == 0):
    divisivel = "é divisivel"
else:
    divisivel = "não é divisivel"
print (f"Seu número {divisivel}.")