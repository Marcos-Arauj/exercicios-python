from random import randint

print('=' * 50)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=' * 50)

cont = 0

while True:
    valor = int(input('Digite um valor: '))
    jogador = ' '

    while jogador not in 'PI':
        jogador = input('Par ou ímpar? [P/I]\n').upper().strip()[0]
    print('-' * 50)

    computador = randint(0, 10)
    soma = valor + computador
    total_soma = ''

    if soma % 2 == 0:
        total_soma = 'P'
        print(
            f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU PAR')
        print('-' * 50)
    else:
        total_soma = 'I'
        print(
            f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        print('-' * 50)

    if jogador == total_soma:
        print('Você venceu!!!\n'
              'Vamos jogar novamente...')
        print('=' * 50)
        cont += 1
    else:
        print('Você Perdeu!!!\n')
        print('=' * 50)
        break

print(f'GAME OVER! Você venceu {cont} vezes!')
