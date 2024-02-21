palaras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
'MERCADO', 'PROGRAMADOR', 'FUTURO')
print("-"*40)
print(f'{"Separando as vogais":-^40}')
print("-"*40)

for c in range(0, len(palaras)):
    print(f'\nNa palavra {palaras[c]} temos ',end='')
    for letra in palaras[c]:
        if letra in 'AEIOU':
            print(letra, end=' ')
