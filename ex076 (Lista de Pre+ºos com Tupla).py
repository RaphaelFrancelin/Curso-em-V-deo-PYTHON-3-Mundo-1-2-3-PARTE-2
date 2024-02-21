listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas',22.3,
            'Livro', 34.9)
print("-"*40)
print(f'{"Listagem de Preços":^40}')
print("-"*40)

for c in range(0, len(listagem)): #Aqui coloca cada item em uma linha
    if c % 2 == 0: # separa todas as linhas pares, ou seja, separa a linha que está o nome dos itens
        print(f'{listagem[c]:.<30}',end=" ") #printa alinhado a esquerda com trinta caracteres
    else:
        print(f'R${listagem[c]:>7.2f}') # printa as linhas impares,
                                        # alinhado a direita com 7 caracteres com duas casas deposi da virgula
print("-"*40)
print(f'{"FIM":^40}')