"""
Execício
Peça ao usuário para digitar seu nome
peça ao usuário para digitar idade
se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        seu nome invertido é {nome invertido}
        seu nome contém (ou não) espaços
        seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Deculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

espc = ' '
if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Sua idade é {idade}.')
    print(f'Seu nome invertido ficará assim: {nome[::-1]}')
    if espc in nome:
        print(f'Seu nome contém espaçõs')
    else:
        print(f'Seu nome não contem espaçõs')
    print(f'Seu nome contem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
   input(f'Deculpe, você deixou campos vazios')