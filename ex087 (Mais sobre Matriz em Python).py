#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPares = 0
somaTerceiraColuna = 0
maiorValorSegundaLinha = 0
for linha in range (0,3):
    for coluna in range (0,3):
        matriz [linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
somaTerceiraColuna = matriz[0][2] + matriz[1][2] + matriz[2][2]
if matriz[1][0] > maiorValorSegundaLinha:
    maiorValorSegundaLinha = matriz[1][0]
if matriz[1][1] > maiorValorSegundaLinha:
    maiorValorSegundaLinha = matriz[1][1]
if matriz[1][2] > maiorValorSegundaLinha:
    maiorValorSegundaLinha = matriz[1][2]

print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')
print(f'A soma de todos os valores pares digitados é de {somaPares}.')
print(f'A soma dos valores da terceira coluna é de {somaTerceiraColuna}.')
print(f'O maior valor da segunda linha é de {maiorValorSegundaLinha}.')
