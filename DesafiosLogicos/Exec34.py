h = float(input("Digite sua altura: "))
sexo = str(input("DIgite seu sexo, M para mulher e H para homem: "))[0]

if (sexo == "M"):
    print (f"O seu peso ideal é {(62.1*h) - 44.7}. ")
elif (sexo == "H"):
    print (f"Seu peso ideial é {(72.7*h) - 58}. ")