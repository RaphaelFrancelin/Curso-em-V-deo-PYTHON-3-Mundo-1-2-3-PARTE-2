


while True:
    numero = int(input('Deseja adicionar qual número na lista? '))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str('Deseja continuar [S/N]: ').upper().strip()[0]

    listaNumero = [numero]

    if continuar == 'N':
        print(listaNumero)
        break


