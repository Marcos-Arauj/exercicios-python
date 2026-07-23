lista_produto = []
lista_valor = []
valor_total = 0
produtos_caros = 0

for i in range(1, 6):

    produto = input('Informe o produto que você deseja acidionar ao carrinho: ').upper().strip()
    preco = float(input('Informe o preço do produto: R$'))
    valor_total += preco 

    lista_produto.append(produto)
    lista_valor.append(preco)

    if preco > 100:
        produtos_caros += 1

posicao_maior = lista_valor.index(max(lista_valor))
posicao_menor = lista_valor.index(min(lista_valor))
produto_caro = lista_produto[posicao_maior].lower()
produto_barato = lista_produto[posicao_menor].lower()

print(f'O produto mais caro é {produto_caro} que custa R${max(lista_valor):.2f}\n'
      f'O produto mais barato é {produto_barato} que custa R${min(lista_valor):.2f}\n'
      f'VALOR TOTAL = R${valor_total:.2f}\n'
      f'A quantidade de produtos que custam mais de R$100 é de {produtos_caros}')


    

    

