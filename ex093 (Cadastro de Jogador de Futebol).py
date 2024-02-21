jogador = dict()
partidas = list()

jogador['Nome do Jogador'] = str(input('Qual o Nome do Jogador: '))
totalDePartidas = int(input(f'Quantas partidas o jogador {jogador["Nome do Jogador"]} jogou:  '))

for c in range (0,totalDePartidas):
   partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['Gols por Partidas'] = partidas[:]
jogador['Total de Gols'] = sum(partidas)
print('-='*20)
print(jogador)

print('-='*20)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*20)
print(f'O Jogador {jogador["Nome do Jogador"]} jogou {totalDePartidas} partidas.')
for i, v in enumerate(jogador['Gols por Partidas']):
    print(f'=> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total de Gols"]}')
