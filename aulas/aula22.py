# Operadores Lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso,
# a expressão inteira serpa invpalida naquele ValueErrorSão considerador falsy
# 0 0.0 '' False
# Também existe o tipo de dado "None" que ´r usado para representar um não valor

#Simulando um sistema de login e senha
entrada = input('[E]ntrar ou [S]air: ')
senha = input('Senha: ')

# # Simulando um banco de dados
senha_valida = '12345'

if (entrada == 'E' or 'e') and senha_valida == senha:
    print('Entrar')
else:
    print('Sair')


# Avaliação de cirto circuito com "and"
# print(True and False and 0 and True)
# Em um curto sempre que houver um valor for "Falso" ou equivalente, toda a linha será falso


# Avaliação de cirto circuito com "or"
# print(0 or False or True or 'abc')
# Assim que o primeiro valor for "True" ou equivalente, toda a linha será verdadeira


# Avaliação de cirto circuito com "or"
# senha = input('Senha: ') or 'Sem senha'
# print(senha)
# Assim que o primeiro valor for "True" ou equivalente, toda a linha será verdadeira