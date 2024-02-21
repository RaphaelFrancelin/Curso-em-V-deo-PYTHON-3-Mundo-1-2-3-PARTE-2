numeros = list()
maiorNumero = 0
menorNumero = 0

for posição in range(0,5):
    numeros.append(int(input(f'Digite um valor para a Posição {posição}: ')))

    if posição == 0:
        maiorNumero = menorNumero = numeros[posição]
    else:
        if numeros[posição] > maiorNumero:
            maiorNumero = numeros[posição]
        if numeros[posição] < menorNumero:
            menorNumero = numeros[posição]

print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maiorNumero} e na posições ',end='')
for i, v in enumerate(numeros):
    if v == maiorNumero:
        print(f'{i}... ',end='')
print(f'\nO menor valor digitado foi {menorNumero} e na posições ',end='')
for i, v in enumerate(numeros):
    if v == menorNumero:
        print(f'{i}... ',end='')
