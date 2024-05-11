nome = input('Nome: ')
altura = float(input('Altura: '))
peso = int(input('Peso: '))
imc = ... 
imc = int(peso / (altura * altura))


print('O fulano:', nome, 'tem', altura, 'de altura.')
if imc == 20:
    print('Esta pesando:', peso, 'e esta com o IMC de:', imc, 'você esta no peso ideal')
if imc >= 21:
    print('Esta pesando:', peso, 'e esta com o IMC de:', imc, ' você esta acima do peso')

#print('Esta pesando:', peso, 'e esta', imc)