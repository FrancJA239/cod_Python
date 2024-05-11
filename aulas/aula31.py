"""
Flag (Bandeira) - Marcar um local
Nome = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

# v1 = 'a'
# v2 = 'b'

# # os "id" dão identificação aos objetos ou informações que guardamos na memoria
# # se o código for executado, poreremos ver que cada "v" etem um "id" diferente
# print(id(v1))
# print(id(v2))
# condicao

condicao = True
passou_no_if = None
# esta condição não tem valor, e servira para avaliar se irá passar pelo "if"

if condicao: # caso minha "condicao" seja verdadeira meu cod irá passar pelo "if"
     passou_no_if = True # neste momneto minha condição tem valor assim que passar pelo "if"
     print('Faça algo')
else: # caso minha "condicao" não seja mais verdadeira, meu cod irá passar pelo "else"
   print('Não faça algo')

print(passou_no_if, passou_no_if is None)
# caso a variável "passou_no_if" ainda esteja sem valor, deve dizer que é none "is none"
print(passou_no_if, passou_no_if is not None)
# caso a variável "passou_no_if" agora tenha um valor, deve dizer que não é none "is not none"

# Simplificando
if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')