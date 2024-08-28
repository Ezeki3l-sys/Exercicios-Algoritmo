palavra = str(input("Digite uma palavra: : ").upper().replace(" ",""))
arvalap = palavra[::-1]
palindromo = True if palavra == arvalap else False

if (palindromo==True):
    print ("É palindrômo. ")
else:
    print ("Não é palindrômo. ")