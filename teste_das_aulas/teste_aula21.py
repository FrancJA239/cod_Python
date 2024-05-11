# Operadores Lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso,
# a expressão inteira serpa invpalida naquele ValueErrorSão considerador falsy
# 0 0.0 '' False
# Também existe o tipo de dado "None" que ´r usado para representar um não valor

#Simulando um sistema de login e senha
entrada = input('[E]ntrar ou [S]air: ')
email = input('E-mail: ')
senha = input('Senha: ')

# Simulando um banco de dados
senha_valida = 'Ahpuch0239'
senha_idiota = '123'
email_valido = 'Ahpuch@python'

# Funcionamento do sistema -> Resposta do sistema

if entrada == 'E' and email == email_valido:
    print(
        'E-mail válida'
        )
elif entrada == 'E' and email != email_valido:
    print(
        'E-mail incorreto!'
          )
elif entrada == 'E' and senha != senha_valida:
    print(
        'Senha Incorreta!'
          )
elif entrada == 'E' and senha == senha_idiota:
    print(
        'Ta me zuando porra?'
        )
elif entrada == 'E' and senha == senha_valida:
    print(
        'Senha válida'
        )
else:
    print('Você saiu do sistema')
# Refazer todo o cod!!!!

print('####################### Bem Vindo ao Inf. (Zuera!!) ###########################')
print('HAHAHAHAHAHAHAHAHAH')
print('HAHAHAHAHAHAHAHAHAH')
print('HAHAHAHAHAHAHAHAHAH')
print('###############################################################################')