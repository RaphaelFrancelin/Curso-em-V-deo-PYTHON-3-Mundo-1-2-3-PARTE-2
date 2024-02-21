
total_preco = 0
contador_preco = 0
maior_preco = 0
menor_preco = 0
contador = 0
nome_Mais_Barato = ' '
nome_Mais_Caro = ' '
while True:
    nome_do_produto = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$ '))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Que continuar? [S/N] ')).upper().strip()[0]
    contador += 1

    total_preco += preco

    if preco >= 1000:
        contador_preco += 1

    if contador == 1:
        nome_Mais_Barato = nome_do_produto
        nome_Mais_Caro = nome_do_produto
        maior_preco = preco
        menor_preco = preco
    if preco > maior_preco:
        nome_Mais_Caro = nome_do_produto
        maior_preco = preco
    if preco < menor_preco:
        nome_Mais_Barato = nome_do_produto
        menor_preco = preco

    if continuar == 'N':
        print(f'Total gatos na Compra foi de R${total_preco:.2f}')
        print(f'{contador_preco} produto custa mais de R$1000.00')
        print(f'O Produto mais Barato é {nome_Mais_Barato} e custou R${menor_preco:.2f}')
        print(f'O Produto mais caro é {nome_Mais_Caro} e custou R${maior_preco:.2f}')
        break
print('Fim do Programa')