aluno = dict()

aluno['nome'] = str(input("Nome do Aluno: "))
aluno['média'] = float(input(f'Qual a média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] =  'APROVADO'
elif aluno['média'] < 5:
    aluno['situação'] = 'REPROVADO'
else:
    aluno['situação'] = 'RECUPERAÇÃO'

print('-=' * 30)
for k, v in aluno.items():
    print(f'-{k} é igual a {v}.')
