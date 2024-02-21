cadastro = list()
pessoa = dict()
somaDeIdade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro Digite somente M para masculino ou F para feminino.')
    pessoa['idade'] = int(input('Idade: '))
    somaDeIdade += pessoa['idade']
    cadastro.append(pessoa.copy())
    while True:
        continuar = str(input('Deseja continuar [S/N]? ')).upper()[0]
        if continuar in 'SN':
            break
        print('Erro Digite somente S para sim ou N para Não.')
    if continuar == 'N':
        break

print(f'A) Foram cadastradas {len(cadastro)} pessoas')
print(f'B) A média de idade é de {(somaDeIdade / len(cadastro)):5.2f}')#cinco casa e duas decimais
print(f'C) O nome de todas as mulheres cadastradas ', end='')
for p in cadastro:
   if p['sexo'] in 'Ff':
       print(f'{p["nome"]} ', end='')
print()
print(f'D) Nome das pessoas cadastradas com idade acima da média ',end='')
for p in cadastro:
    if p['idade'] >= (somaDeIdade/len(cadastro)):
        print(f'{p["nome"]} de {p["idade"]} anos de idade ',end='')