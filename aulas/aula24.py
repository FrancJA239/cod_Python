# Operadores in e not in
# strings são iteráveis
#  0 1 2 3 4 5
#  A h p u c h
# -6-5-4-3-2-1

# nome = 'Ahpuch'
# print(nome[4])
# print(nome[-2])
# print('zero' in nome)
# print(10 * '-')
# print('puc' not in nome)
# print('zero' not in nome)
# Neste caso eu consigo buscar a quarta letra do nome "Ahpuch"
# pois significa que esta entre as letras, significado de "in"

nome = input('Digite seu nome: ')
encontrar = input('Digite o que esta procurando: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')