pessoas = []
listaPessoas = []
pessoasMaiorPeso = pessoasMenorPeso = list()
maiorPeso = menorPeso = 0

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))

    if len(listaPessoas) == 0:
        maiorPeso = menorPeso = pessoas[1]
    else:
        if pessoas[1] >= maiorPeso:
            maiorPeso = pessoas[1]
        if pessoas[1] <= menorPeso:
            menorPeso = pessoas[1]

    listaPessoas.append(pessoas[:])
    pessoas.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Listagem de cadastrados{listaPessoas}.')
print(f'Foram cadastrados {len(listaPessoas)} pessoas')
print(f'Maior peso {maiorPeso} Kgs. Lista de nomes dos mais pesados ',end='')
for p in listaPessoas:
    if p[1] == maiorPeso:
        print(f'[{p[0]}]',end='')
print()
print(f'Menor peso {menorPeso} Kgs. Lista de nomes dos mais leves ',end='')
for p in listaPessoas:
    if p[1] == menorPeso:
        print(f'[{p[0]}] ',end='')
print()