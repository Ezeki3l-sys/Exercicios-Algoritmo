populacaoA = 80000
populacaoB = 200000
anos = 0
while (populacaoA<=populacaoB):
    print(f"Ano {2024+anos}: País A {round(populacaoA)} X País B {round(populacaoB)}. ")
    populacaoA = populacaoA*1.03
    populacaoB = populacaoB*1.015
    anos=anos+1