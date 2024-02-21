from lib1.interface import *
from lib1.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu('Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema')
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo so sistema... Até logo!')
        break
    else:
        print(f'\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)

