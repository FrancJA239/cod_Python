"""
Interpolação básica de strings
s - string
d e i - int
x e X - hexadecimal (ABCDEF0123456789)
"""

nome = 'Ahpuch'
preco = 100.000
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)