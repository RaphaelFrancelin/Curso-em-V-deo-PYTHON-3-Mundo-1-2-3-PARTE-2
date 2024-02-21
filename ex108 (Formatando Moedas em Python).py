from utilidadescev import moedas

preco = float(input('Digite o Preço R$: '))
print(f'A metade de {moedas.moeda(preco)} é {moedas.moeda(moedas.metade(preco))}')
print(f'O dobro de {moedas.moeda(preco)} é {moedas.moeda(moedas.dobro(preco))}')
print(f'Aplicando um aumento de 10% de R${moedas.moeda(preco)} ficaria {moedas.moeda(moedas.aumentar(preco,10))}')
