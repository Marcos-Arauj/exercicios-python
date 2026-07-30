numero = int(input('Digite um número: '))
primo = True

if numero < 2:
    print('Não é primo')
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False

    if primo:
        print('É primo')
    else:
        print('Não é primo')

