sim = 0
decisao = ""

decisao = str(input("Telefonou para a vítima? "))
if (decisao == "sim"):
    sim = sim +1
decisao = str(input("Esteve no local do crime? "))
if (decisao == "sim"):
    sim = sim +1
decisao = str(input("Mora perto da vítima? "))
if (decisao == "sim"):
    sim = sim +1
decisao = str(input("Devia para a vítima? "))
if (decisao == "sim"):
    sim = sim +1
decisao = str(input("Já trabalhou com a vítima? "))
if (decisao == "sim"):
    sim = sim +1

if (sim == 2):
    print("Suspeito")
elif (sim >=3 and sim<=4):
    print("Cúmplice")
elif (sim == 5):
    print("Assassino")
else:
    print("inocente")