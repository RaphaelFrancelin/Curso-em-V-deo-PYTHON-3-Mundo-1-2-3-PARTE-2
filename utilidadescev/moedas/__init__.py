def aumentar(preco, taxa):
    return preco + (preco * taxa / 100)


def diminuir(preco = 0, taxa = 0):
    return preco - (preco * taxa/100)

def dobro(preco = 0):
    return preco * 2


def metade(preco = 0):
    return preco / 2

def moeda(preco = 0, moeda = 'RS '):
    return f'{moeda}{preco:.2f}'


def resumo(preco=0, aumento=0, desconto=0):
    print('~'*30)
    print('RESUMO DO VALOR'.center(30))
    print('~' * 30)
    print(f'Preço Analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{moeda(dobro(preco))}')
    print(f'Metade do preço: \t{moeda(metade(preco))}')
    print(f'{aumento}% de aumento: \t{moeda(aumentar(preco,aumento))}')
    print(f'{desconto}% de redução: \t{moeda(diminuir(preco,desconto))}')
    print('-'*30)