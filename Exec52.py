numero = int(input("Digite um número: "))
primo = True
divisoes = 1
primos=[2]
for n in range (1, numero+1,2):
    contador = n - 1 
    while (contador>1):
        primo = True
        if (n%contador==0):
            primo = False      
            break
        contador = contador - 1
        divisoes = divisoes + 1
    if (primo == True and n>1):
        primos.append(n)

print(f'Números primos {primos}')
print (f"O número de divões foi {divisoes}.")    


# IF TERNARIO
#primo = True if n%contador==0  else False
