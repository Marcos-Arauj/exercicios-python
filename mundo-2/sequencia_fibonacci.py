print('='*50)
print('Sequencia de Fibonacci')
print('='*50)

numero = int(input('Quantos termos você quer mostrar? '))
numero1 = 0
numero2 = 1
cont = 0

while cont < numero:
    print(numero1, end=' ')
    sequencia = numero1 + numero2
    numero1 = numero2
    numero2 = sequencia
    cont += 1
