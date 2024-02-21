valor_saque = int(input('Qual valor deseja sacar? R$ '))
total_saque = valor_saque
cedula = 50
contagem_cedula = 0

while True:
    if total_saque >= cedula:
        total_saque -= cedula
        contagem_cedula += 1
    else:
        if contagem_cedula > 0:
            print(f'Total de {contagem_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contagem_cedula = 0
        if total_saque == 0:
            break
print('Fim do Programa')
