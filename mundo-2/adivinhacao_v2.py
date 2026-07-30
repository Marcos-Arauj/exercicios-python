import random

print('Olá usuário! Vamos jogar um jogo de adivinhação?\n' \
'Estou pensando em um número de entre 0 e 10, tente adivinhar!!!')

numero = int(input('Qual o seu palpite? '))
contador = 1
n_computador = random.randint(0, 10)

while numero != n_computador:
    if n_computador > numero:
        print('Mais... Tente mais uma vez')
    else:
        print('Menos... Tente mais uma vez')
    numero = int(input('Qual o seu palpite? '))
    contador += 1

if contador == 1:
    print(f'Você acertou! O número que eu pensei foi {n_computador} e você tentou apenas {contador} vez.')
else:
    print(f'Você acertou! O número que eu pensei foi {n_computador} e você tentou {contador} vezes.')