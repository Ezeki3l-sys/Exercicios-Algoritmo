import math

a = int(input("Digite o coeficiente A: "))
b = int(input("Digite o coeficiente B: "))
c = int(input("Digite o coeficiente C: "))

if (a != 0 and b != 0 and c != 0):
    delta=b*b-4*a*c
    if (delta < 0): 
      print ("Não é possível fazer a conta")
    else:
        x1 = (-b + math.sqrt(delta, 2)) / (2*a)
        x2 = (-b - math.sqrt(delta, 2)) / (2*a)
        if(delta == 0):
            print ("A sua raíz é ",x1)
        if (delta > 0):
            print ("Suas raízes são ", x1," e ", x2)
