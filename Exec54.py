valores = {
    "[0-25]": 0,
    "[26-50]": 0,
    "[51-75]": 0,
    "[76-100]": 0
}
numero = 0

while (numero>=0):
    numero = int(input("Digite um número entre 0 e 100: "))
    #if (numero>=0 and numero<=25): x   
    if (0 <= numero <=25):
        print(numero)
        valores["[0-25]"] = valores["[0-25]"] + 1
    elif (numero>25 and numero<=50):
        valores["[26-50]"] = valores["[26-50]"] + 1
    elif (numero>50 and numero<=75):
        valores["[51-75]"] = valores["[51-75]"] + 1
    elif (numero>75 and numero<=100):
        valores["[76-100]"] = valores["[76-100]"] + 1

print (valores)
