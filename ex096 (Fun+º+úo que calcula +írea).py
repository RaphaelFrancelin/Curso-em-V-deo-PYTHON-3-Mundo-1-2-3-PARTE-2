def área(l, c):
    total= l * c
    print(f'A área do terreno informada é de {l} metros de largura por {c} metros de comprimento totalizando uma área de {total}m².')

print('----Controle de terrenos----')
l= float(input('Digite a Largura do terreno em metros: '))
c= float(input('Digite o Comprimento do terreno em metros: '))
área(l, c)