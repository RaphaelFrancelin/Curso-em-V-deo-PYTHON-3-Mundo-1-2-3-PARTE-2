from datetime import datetime
cadastro = {
    'nome': str(input('Qual seu nome: ')),
    'idade': int(input('Qual seu ano de nascimento: ')),
    'ctps': int(input('Qual número da sua carteira de trabalho, se não tiver digite 0: '))}
if cadastro['ctps'] > 0:
    cadastro['contratação']= int(input('Qual ano de Contratação: '))
    cadastro['salário']= float(input('Qual seu salário: '))
    cadastro['idade'] = datetime.now().year - cadastro['idade']
    cadastro['aposentadoria'] = ((cadastro['contratação'] + 35) - datetime.now().year) + cadastro['idade']
print('-='*15)
for k,v in cadastro.items():
    print(f'- {k} tem o valor {v}.')
