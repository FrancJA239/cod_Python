"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que você digitar: ')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#Neste caso acabei criando uma nova variavel para informar que o valor da "str" é "flt"
#     print(f'O drobro do {numero_str} é {numero_float * 2:.0f}')
# else:
#     print(f'Voc^não digitou um número')

try: #try é usado para criar uma condição, praticamente uma mudança de fluxo no código
    print('Str:', numero_str)
    numero_float = float(numero_str)
    print('Float: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
except: #except é usado para criar o segundo caminho após o "try", caso o mesmo tenha um erro o except será executado
    print(f'{numero_str} Não é um, número')