listaNumeros = [[],[]]
numerosAdicionados= 0
for c in range (1,8):
    numerosAdicionados = int(input(f'Digite o {c}º Número:  '))
    if numerosAdicionados % 2 == 0:
        listaNumeros[0].append(numerosAdicionados)
    else:
        listaNumeros[1].append(numerosAdicionados)

print(f'Os valores digitados foram {listaNumeros}')

listaNumeros[0].sort()
listaNumeros[1].sort()

print(f'Os valores pares são: {listaNumeros[0]}.')
print(f'O valores impares são: {listaNumeros[1]}.')
