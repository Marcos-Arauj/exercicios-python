import time

print('Olá usuário! Para que o menu seja mostrado, preciso primeiro que você digite dois valores.')

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))

print('\t [1] somar\n' \
'\t [2] multiplicar\n' \
'\t [3] maior\n' \
'\t [4] novos números\n' \
'\t [5] sair do programa')

while True:
    opcao = input('Escolha uma opção: ')

    match opcao:
        case '1':
            soma = v1 + v2
            time.sleep(1)
            print(f'A soma entre os dois valore é {soma}')
            print('='*50)
        case '2':
            multiplicar = v1 * v2
            time.sleep(1)
            print(f'O produto entre os dois valores é {multiplicar}')
            print('='*50)
        case '3':
            if v1 > v2:
                time.sleep(1)
                print('O maior valor é o primeiro!')
            elif v1 < v2:
                time.sleep(1)
                print('O maior valor é o segundo')
            else:
                time.sleep(1)
                print('Os valores são iguais!')
        case '4':
            v1 = int(input('Digite o primeiro valor novamente: '))
            v2 = int(input('Agora digite o segundo valor novamente: '))
            print('\t [1] somar\n' \
                '\t [2] multiplicar\n' \
                '\t [3] maior\n' \
                '\t [4] novos números\n' \
                '\t [5] sair do programa')
        case '5':
            print('Finalizando...')
            time.sleep(2)
            print('Fim do programa!')
            break
        case _:
            print('Número inválido, digite um valor de 1 a 5')
            print('='*50)



