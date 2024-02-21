numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite mais um número: '))
numero4 = int(input('Digite o último número: '))
tuplaDeNumeros = (numero1, numero2, numero3, numero4)

###Resposta do Guanabara para fazer a Tupla####
###num = (int(input('Digite um número: ')),
#           int(input('Digite outro número: ')),
#           int(input('Digite mais um número: ')),
#           int(input('Digite o último número: ')))


print(f'Você digitou os valores {tuplaDeNumeros}')
################pergunta A###########################################
if 9 in tuplaDeNumeros:
    if tuplaDeNumeros.count(9) == 1:
        print('O valor 9 apareceu uma uníca vez')
    else:
        print(f'O valor 9 apareceu {tuplaDeNumeros.count(9)} vezes.')
else:
    print('O valor 9 não pareceu')
##################pergunta B###########################################
if 3 in tuplaDeNumeros:
    print(f'O valor 3 apareceu na {tuplaDeNumeros.index(3)+1}ª posição.')
else:
    print('O valor 3 não apareceu')
##################pergunta C###########################################
print('Os valores pares digitados foram os números ', end='')
for c in tuplaDeNumeros:
    if c % 2 == 0:
        print(c, end=' ')