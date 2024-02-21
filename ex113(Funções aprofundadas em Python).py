def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não informar esse dado!\033[m')
            return 0
        else:
            return n


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não informar esse dado!\033[m')
            return 0
        else:
            return n


numInt = leiaint(input('Digite um Numero Inteiro: '))
numFloat = leiafloat(input('Digite um Numero real: '))

print(f'O valor inteiro digitado foi {numInt} e o real foi {numFloat}')
