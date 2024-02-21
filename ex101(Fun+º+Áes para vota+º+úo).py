import datetime
def voto(ano):
    if dataHoje < 16:
        print(f'Você tem {dataHoje} anos de idade e seu Voto foi NEGADO')
    elif dataHoje >=18 and dataHoje < 65:
        print(f'Você tem {dataHoje} anos de idade e seu Voto é OBRIGATÓRIO')
    else:
        print(f'Você tem {dataHoje} anos de idade e seu Voto OPCIONAL')

anoDigitado=int(input('Digite seu ano de nascimento: '))
dataHoje = datetime.date.today().year - anoDigitado
print(voto(dataHoje))

### RESPOSTA DO GUANABARA
# def voto(ano):
#   from datetime import date
#   atual = date.Today().year
#   if idade < 16:
#       return f'Com {idade} anos: NÃO VOTA.'
#    elif 16 <= idade < 18 or idade > 65:
#       return f'Com {idade} anos: Voto Opcional.'
#     else:
#       return f'Com {idade} anos: Voto Obrigatório.'
#nasc =int(input('Em que ano você nasceu: '))
#print(voto()) ###