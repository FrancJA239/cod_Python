"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^- Centro
Sinal - + ou -
= - força o número a aparecer antes dos zeros
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4165161654646:,.2f}')
print(f'o hexadecimal de 1500 é {1500:08X}')