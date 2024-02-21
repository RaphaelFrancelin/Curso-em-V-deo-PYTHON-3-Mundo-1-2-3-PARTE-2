from time import sleep
def contagem (inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(0.2)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ')
            cont += passo
            sleep(0.5)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            cont -= passo
            sleep(0.5)
    print('FIM')
    print('-=' * 20)

contagem(1, 10, 1)
contagem(10, 0, 1)
print('Agora sua vez, Digite o inicio o Fim e o passo')
inicio= int(input('Inicio: '))
fim= int(input('Fim: '))
passo= int(input('Passo: '))
contagem(inicio,fim,passo)
