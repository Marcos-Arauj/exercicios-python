numero = int(input('Digite um número para saber sua tabuada: '))
operacao = input('Agora digite a operação que você deseja: ').lower().strip()


match operacao:

    case '+':
        for i in range(1, 11):
            print(f'{numero} + {i} = {numero + i}')

    case '-':
        for i in range(1, 11):
            print(f'{numero} - {i} = {numero - i}')

    case '*':
        for i in range(1, 11):
            print(f'{numero} * {i} = {numero * i}')

    case '/':
        for i in range(1, 11):
            print(f'{numero} / {i} = {numero / i:.2f}')

    case _:
        print('Operação inválida! Digite +, -, * ou /')
