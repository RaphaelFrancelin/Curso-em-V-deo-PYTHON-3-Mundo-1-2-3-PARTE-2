from random import randint
from time import sleep
from operator import itemgetter
jogador = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)}
ranking= list()
for k,v in jogador.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)#O itemgetter está ordenando pelo valor [1] que é valor randint, se colocar o valor[0] vai ser ordenado pelo jogador.
print('         ===RANKING===')
for i, v in enumerate(ranking):
    print(f'    {i+1}º Lugar: {v[0]} com {v[1]} pontos')
    sleep(1)
