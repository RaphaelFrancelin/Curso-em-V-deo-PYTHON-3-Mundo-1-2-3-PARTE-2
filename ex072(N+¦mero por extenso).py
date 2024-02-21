numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

opcao = int(input('Digite um Número entre 0 e 20: '))
while opcao < 0 or opcao > 20:
    opcao = int(input('Valor inválido, Digite um Número entre 0 e 20: '))

print(f'Você Digitou o número {numeros[opcao]}')