def fatorial(n, show=False):
    """
    ->calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fator = 1
    for c in range (n, 0 , -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('X',end=' ')
            else:
                print('=',end=' ')
        fator*=c

    return fator

print(fatorial(n=5,show=True))
help(fatorial)
