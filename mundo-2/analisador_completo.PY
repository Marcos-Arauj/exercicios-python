lista_nome = []
lista_idade = []
maior_idade_homem = 0
mais_velho = ''
mulher_mais_nova = 0
media = 0

for i in range (1, 5):
    nome = input('Digite o seu nome: ').strip().capitalize().upper()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite o seu sexo (M ou F): ').strip().capitalize().upper()
    media += idade
    lista_nome.append(nome)
    lista_idade.append(idade)

    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            mais_velho = nome
    elif sexo == 'F':
        if idade < 20:
            mulher_mais_nova += 1
        

print(f'A média de idade do grupo é {media / 4}!\n'
      f'A quantidade de mulheres que têm menos de 20 anos é {mulher_mais_nova}!\n'
      f'O nome do homem mais velho é {mais_velho.title()}!')