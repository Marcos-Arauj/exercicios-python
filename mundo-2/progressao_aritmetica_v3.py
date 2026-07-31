primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
cont = 0

while cont < 10:
    print(termo, end='')
    print(' →' if cont < 9 else '', end=' ')
    termo += razao
    cont += 1

if cont == 10:
    
    while True:
        novo_termo = int(input('\nQuantos termos a mais você quer ver? '))
        novo_cont = cont + novo_termo

        while cont < novo_cont:
            print(termo, end=' ')
            print('→' if cont < novo_cont - 1 else '', end=' ')
            termo += razao
            cont += 1

        if novo_termo == 0:
            print('Encerrando o programa!')
            break
