from random import randint
from time import sleep
quantidadeDeJogos=int(input(f'Digite quantos palpites deseja: '))
print()
print(f'{"_-"*3} {quantidadeDeJogos} Palpites de Jogos da Mega {"_-"*3}')

for c in range(0,quantidadeDeJogos):
    resultado=[]
    for n in range(0,6):
        numerosSorteados= randint(0,60)
        while numerosSorteados in resultado:
            numerosSorteados = randint(0, 60)
        resultado.append(numerosSorteados)
    resultado.sort()

    print(f'Jogo {c+1}: {resultado}')
    sleep(1)
print('_-'*20)