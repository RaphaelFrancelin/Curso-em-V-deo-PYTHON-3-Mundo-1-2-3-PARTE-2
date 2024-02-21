from random import randint

numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Números sorteados: {numeros}')
print(f'Maior valor sorteado: {max(numeros)}')
print(f'Menor valor sorteado: {min(numeros)}')
for n in numeros:
    print(f'{n} ', end='')
