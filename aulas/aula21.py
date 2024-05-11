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

# Simulando um banco de dados
senha_valida = '12345'

if entrada == 'E' and senha_valida == senha:
    print('Entrar')
else:
    print('Sair')