valores = []
for n in range (0,4):
    valores.append(float(input("Digite um valor decimal: ")))
media = (valores[0]+valores[1]+valores[2]+valores[3])/4
print(f"A média é {media}.")
print("E os números fora da média são: ")
for n in range (0,4):
    if (valores[n]>media):
        print(valores[n])