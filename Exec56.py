extenso = [{ "um": 1, "dois": 2, "três": 3, "quatro": 4, "cinco": 5, "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10, "onze": 11, "doze": 12, "treze": 13, "quatorze": 14, "quinze":15, "dezesseis": 16, "dezesete": 17, "dezoito": 18, "dezenove": 19, "vinte": 20 },{"noventa": 90,"oitenta": 80, "setenta": 70, "sessenta": 60, "cinquenta": 50, "quarenta": 40, "trinta": 30, "vinte": 20}]
numero = int(input("Digite um número: "))
resultado =""
if (numero<=20):
        for k,v in extenso[0].items():
            if (numero==v):
                print(k)
else:
     numeroD = numero-numero%10
     for k,v in extenso[1].items():
          if (numeroD==v):
               resultado=k    
     if (numero%10!=0):
         numeroU = numero%10
         for l in extenso:
              for k,v in l.items():
                   if(v==numeroU):
                        resultado+= " e "+ k
                        #resultado= "e".join(resultado, k)
     print(resultado)
     [   
          [[1], [2], [3]],
          [[4], [5], [6]]
     ]