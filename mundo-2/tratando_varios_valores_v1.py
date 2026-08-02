numero = int(input('Digite um número [999 para parar]: '))
cont = 0
soma = 0

while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número [999 para parar]: '))


print(f'A quantidade de números digitados foi {cont} e a soma entre eles foi {soma}!')