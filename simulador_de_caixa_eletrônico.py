valor_sacado = int(input('Qual o valor a ser sacado: R$'))
qtde_50 = valor_sacado // 50
resto_50 = valor_sacado % 50
qtde_20 =  resto_50 // 20
resto_20 = resto_50 % 20
qtde_10 = resto_20 // 10
resto_10 = resto_20 % 10
qtde_1 = resto_10 // 1
resto_1 = resto_10 % 1

if qtde_50 > 0:
    print(f'Total de {qtde_50} cédulas de R$50')
if qtde_20 > 0:
    print(f'Total de {qtde_20} cédulas de R$20')
if qtde_10 > 0:
    print(f'Total de {qtde_10} cédulas de R$10')
if qtde_1 > 0:
    print(f'Total de {qtde_1} cédulas de R$1')