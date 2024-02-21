listaDeAlunos = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/ 2
    listaDeAlunos.append([nome, [nota1, nota2], media])
    resposta = str(input('Deseja Continuar [S/N]: '))
    if resposta in 'Nn':
        break
print(listaDeAlunos)
print('_'*30)
print(f'{"Id":<4}{"NOME":<10}{"MEDIA":>6}')
print('-'*30)

for id, correListaDeAluno in enumerate(listaDeAlunos):
    print(f'{id:<4}{correListaDeAluno[0]:<10}{correListaDeAluno[2]:>6}')