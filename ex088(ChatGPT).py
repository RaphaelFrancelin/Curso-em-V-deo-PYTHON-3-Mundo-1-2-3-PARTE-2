import random

quantidadeDeJogos = int(input('Digite quantos palpites deseja: '))

for c in range(0, quantidadeDeJogos):
    resultado = random.sample(range(1, 61), 6)

    # Centralizando os números na saída
    resultado_formatado = [str(num).center(3) for num in resultado]
    print(f'Jogo {c + 1}: [{" ".join(resultado_formatado)}]')
