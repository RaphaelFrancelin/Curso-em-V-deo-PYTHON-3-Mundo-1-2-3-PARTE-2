times = ('Botafogo', 'Flamengo', 'Grêmio', 'São Paulo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Athletico-PR', 'Fortaleza', 'Cruzeiro',
         'Internacional', 'Atlético-MG', 'Cuiabá', 'Santos', 'Corinthians', 'Bahia', 'Goiás', 'Cotitiba', 'Vasco da Gama', 'América-MG')
print(f'Lista de Times do Brasileirão: {times}')
print(20*"-=")
print(f'Os 5 Primeiros são: {times[0:5]}')
print(20*"-=")
print(f'Os 4 últimos são: {times[-4:]}')
print(20*"-=")
print(f'Todos os times em ordem: {sorted(times)}')
print(20*"-=")
print(f'O Corinthians está na {times.index("Corinthians")+1}ª posição')
print(20*"-=")
