n1 = 1
n2 = 0
fim = int(input("DIgite um valor: "))

while (fim>=1):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    fim = fim - 1
print (f"O número da sequência é {n3}.")