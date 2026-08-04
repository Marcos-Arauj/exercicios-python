total = qtde_produtos = 0

produto = input('Nome do produto: ').capitalize().strip()
preco = float(input('Preço: R$'))

menor_preco = preco
produto_barato = produto

while True:
    total += preco
    
    if preco >= 1000:
        qtde_produtos += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if continuar == 'N':
        break

    produto = input('Nome do produto: ').capitalize().strip()
    preco = float(input('Preço: R$'))

    if preco < menor_preco:
        menor_preco = preco
        produto_barato = produto
    
print(f'Total gasto: {total:.2f}\n'
      f'Quantidade de produtos acima de R$1000: {qtde_produtos}\n'
      f'Produto mais barato: {produto_barato} (R${menor_preco})')
print('Fim do programa.')