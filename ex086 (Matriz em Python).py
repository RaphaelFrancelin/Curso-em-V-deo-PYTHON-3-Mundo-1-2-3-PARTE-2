matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range (0,3):
    for coluna in range (0,3):
        matriz[linha] [coluna] = int(input(f'Digite um valor para posição [{linha}, {coluna}]: '))

print(f'Minha Resposta')
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')

print(f'Resposta do Guanabara')
for linha in range(0,3):
    for coluna in range (0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()