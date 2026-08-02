numero = int(input('Digite um número: '))
lista_valores = []
soma = cont = 0

while True:
    parar = input('Quer continuar? (S/N) ').upper().strip()[0]

    while parar != 'S' and parar != 'N':
        print('Valor inválido!')
        parar = input('Quer continuar? (S/N) ').upper().strip()[0]

    soma += numero
    cont += 1
    lista_valores.append(numero)
    maior = max(lista_valores)
    menor = min(lista_valores)

    match parar:
        case 'S':
            numero = int(input('Digite um número: '))
        case 'N':
            print('Fim do programa.')
            break

media = soma / cont

print(f'Você digitou {cont} números e a média foi {media:.2f}')

if cont == 1:
    print(f'O único valor digitado foi {numero}!')
else:
    print(f'O maior valor digitado foi {maior} e o menor foi {menor}!')