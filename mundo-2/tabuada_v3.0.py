numero = int(input('Digite um número para saber sua tabuada: '))

while True:
    if numero < 0:
        print('Fim do programa.')
        break

    print('=' * 50)

    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

    print('=' * 50)

    numero = int(input('Digite um número para saber sua tabuada: '))