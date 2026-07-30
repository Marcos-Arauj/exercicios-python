frase = input('Digite uma frase: ').lower().strip()
sem_espacos = frase.replace(' ', '')


if sem_espacos == sem_espacos[::-1]:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
