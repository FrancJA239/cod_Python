# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if senha == '123456':
    print('Senha válida')
if not senha == '123456': # nesse caso estou invertendo a expressão
    print('Senha incorreta')
if not senha: 
    print('Você não digitou nada')
# nesse caso estou invertendo a lógica, informando que se não tiver nada na variável "senha" ela se torna falsa