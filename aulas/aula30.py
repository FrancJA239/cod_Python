"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Constagem de complexidade (ruim)
"""

# velocidade = input('Qual a velocidade do veículo: ')
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1 
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

if velocidade > RADAR_1:
    print(f'O veículo passou o limiete de velocidade de {RADAR_1}Km/s')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print(f'O veículo foi multado por ultrapassar o limite de velocidade de {RADAR_1}Km/s')

# print(f'O veículo não ultrapassou o limiete de velocidade')