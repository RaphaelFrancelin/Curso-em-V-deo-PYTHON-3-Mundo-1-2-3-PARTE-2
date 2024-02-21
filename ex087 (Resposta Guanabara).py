#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPares = 0
somaTerceiraColuna = 0
maiorValorSegundaLinha = 0

for linha in range (0,3):
    for coluna in range (0,3):
        matriz[linha] [coluna] = int(input(f'Digite um valor para posição [{linha}, {coluna}]: '))

for linha in range(0,3):
    for coluna in range (0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
    print()

print(f'A soma de todos os valores pares digitados é de {somaPares}.')

for linha in range (0,3):
        somaTerceiraColuna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é de {somaTerceiraColuna}.')

for coluna in range (0,3):
    if coluna == 0:
        maiorValorSegundaLinha = matriz[1][coluna]
    elif matriz[1][coluna] > maiorValorSegundaLinha:
        maiorValorSegundaLinha = matriz[1][coluna]
print(f'O maior valor da segunda linha é de {maiorValorSegundaLinha}.')
