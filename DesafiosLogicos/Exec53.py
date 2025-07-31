import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

eleitores = int(input("Digite o número de eleitores: "))
votacao = {
    "1": 0,
    "2": 0, 
    "3": 0
    }

for n in range (1, eleitores+1):
    voto = 4
    while (voto>3 or voto<1):
        cls()
        voto = int(input("Vote 1 - Bolsonaro\nVote 2 - Lula\nVote 3- Michael\n"))
    votacao[str(voto)] = votacao[str(voto)] +1

print(f"Votos para bolsonaro {votacao["1"]}")
print(f"Votos para Lula {votacao["2"]}")
print(f"Votos para Michael {votacao["3"]}")