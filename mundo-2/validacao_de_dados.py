sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]

while sexo != 'M' and sexo!= 'F':
    print('Opção inválida! Digite M ou F!')
    sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]

if sexo == 'M':
    print('O usuário é do sexo masculino!')
elif sexo == 'F':
    print('O usuário é do sexo feminino!')