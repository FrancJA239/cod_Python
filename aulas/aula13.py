nome = input('Nome: ')
altura = float(input('Altura: '))
peso = int(input('Peso: '))
imc = ... 
imc = int(peso / (altura * altura))

linha_1 = f'O fulano {nome} tem {altura:.2f} de altura.'
linha_2 = f'Esta pesando: {peso}kg e esta com o IMC de: {imc}, você esta no peso ideal'
linha_3 = f'Esta pesando: {peso}kg e esta com o IMC de: {imc}, você esta acima do peso'
# neste caso eu criei uma variável para formatar a linha inteira com o "f"
# em seguida eu acrecentei {} para incluir outras variáveis no texto!

print(linha_1)
if imc == 28:
    print(linha_2)
if imc >= 30:
    print(linha_3)
# Assim posso encurtar o meu cod, deixando ele mai legível e melhor formatado

# print('Esta pesando:', peso, 'e esta', imc)