from datetime import date


maioridade = []
menoridade = []
ano_atual = date.today().year

for i in range(1,8):
    nome = input('Digite seu nome: ')
    ano_nascimento = int(input('Digite o ano que você nasceu: '))
    idade = ano_atual - ano_nascimento

    if idade >= 21:
        maioridade.append(nome)
    else:
        menoridade.append(nome)

print(f'A soma de todos que atingiram a maioridade é {len(maioridade)} e os que ainda não atingiram é {len(menoridade)}!\n'
      f'As pessoas maiores de idade são {', '.join(maioridade)}.\n'
      f'As pessoas menores de idade são {', '.join(menoridade)}.')