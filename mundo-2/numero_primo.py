numero = int(input('Digite um número: '))
primo = True

for i in range(2, numero):
    if numero % i == 0:
        primo = False

if primo:
    print('É primo')
else:
    print('Não é primo')

