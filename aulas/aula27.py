"""
Fatiamento de string
 0123456789
 Olá mundo
-987654321
Fatimaneot [i:f:p] [::]
Obs.: a função "len" retorna a qtd
de caracteres da str
"""
# O fatiamento serve para puxar um caractere em um determinado local
variavel = 'Olá mundo'
print('variavel'[4:7])
print(len(variavel[::-5]))
# A função "len" te retorna a quantidade porem conta o tamando da "str"
print(variavel[0:9:2])
# "0" onde inicia "9" Onde termina "2" numero de caracteres serão pulados
print(variavel[::-1])
# Neste caso estamos invertendo a variável pois irá contar apartir do -1