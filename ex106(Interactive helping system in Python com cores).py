from time import sleep
cores = ('\033[m',           # 0 sem cor
         '\033[0;30;41m',    # 1 vermelho
         '\033[0;30;42m',    # 2 verde
         '\033[0;30;43m',    # 3 amarelo
         '\033[0;30;44m',    # 4 azul
         '\033[0;30;45m',    # 5 roxo
         '\033[7;30m'        # 6 branco
)
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(cores[3], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~'* tam)
    print(f'  {msg}')#esse print formato tem dois espaços para que o titulo não fique colado na tela do lado esquerdo
    print('~'*tam)
    print(cores[0], end='')

#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP',2)
    comando = str(input(f'Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo!!!',1)