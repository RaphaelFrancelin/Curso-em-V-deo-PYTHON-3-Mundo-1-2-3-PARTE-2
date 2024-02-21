from utilidadescev.moedas import moeda
from utilidadescev.moedas import metade
from utilidadescev.moedas import aumentar
from utilidadescev.moedas import dobro
from utilidadescev.moedas import diminuir

preco = float(input('Digite o Preço R$: '))
print(f'A metade de {moeda(preco)} é {moeda(metade(preco))}')
print(f'O dobro de {moeda(preco)} é {moeda(dobro(preco))}')
print(f'Aplicando um aumento de 10% de R${moeda(preco)} ficaria {moeda(aumentar(preco,10))}')
print(f'Aplicando um deconto de 13% de R${moeda(preco)} ficaria {moeda(diminuir(preco,13))}')