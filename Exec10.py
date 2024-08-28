triangulo = ""
ladoA = int(input("Digite o primeiro lado: "))
ladoB = int(input("Digite o segundo lado: "))
ladoC = int(input("Digite o terceiro lado: "))

if (ladoA == ladoB and ladoB == ladoC):
    triangulo = "Triângulo Equilátero."
elif (ladoA == ladoB or ladoB == ladoC or ladoA == ladoC):
    triangulo = "Triângulo Isósceles."
elif (ladoA != ladoB or ladoB != ladoC or ladoA != ladoC):
    triangulo = "Triângulo Escaleno."

print (triangulo)