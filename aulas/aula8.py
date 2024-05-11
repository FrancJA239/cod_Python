

nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
idade = int(input('Idade: '))
ano_nascimento = int(2024 - idade)
maior_de_idade = idade >=18
altura_metros = float(input('Altura em metros: '))

print('#################### Dados Pessoais ###################', end="\n")
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maio de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)