time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome do Jogador'] = str(input('Digite o Nome do jogador: '))
    totalDePartidas = int(input(f'O Jogador {jogador["Nome do Jogador"]} jogos quantas partidas? '))
    partidas.clear()
    for c in range (0,totalDePartidas):
        partidas.append(int(input(f'Quantos gols fez na partida de numero {c+1}? ')))
    jogador['Gols por partida'] = partidas[:]
    jogador['Total de gols'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        continuar = str(input('Deseja continuar [S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('Erro você deve responser somente [S] para sim ou [N] para não. ')
    if continuar == 'N':
        break

print('_'*40)
print('cod.', end=' ')
for i in jogador.keys():
    print(f'{i:<25}', end='')
print()

print('_'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='  ')
    for d in v.values():
        print(f'{str(d):<25}',end='')
    print()
print('_'*40)