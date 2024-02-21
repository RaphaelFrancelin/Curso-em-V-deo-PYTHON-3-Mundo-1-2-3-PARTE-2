from utilidadescev import moedas

preco = float(input('Digite o Preço R$: '))
print(f'A metade de R${preco:.2f} é R${moedas.metade(preco):.2f}')
print(f'O dobro de R${preco:.2f} é R${moedas.dobro(preco):.2f}')
print(f'Aplicando um aumento de 10% R${preco:.2f} fica R${moedas.aumentar(preco,10):.2f}')
