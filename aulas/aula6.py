# Conversão de tipos, coerção
# type convertion, typecasting, coerction
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos
# str, int, float, bool
print(int('1'), + 1) # resultado deve ser "1 1" pois estou separando-os com "int('')"
print(int('1'), type(int('1'))) # Nessa linha estou convertendo minha "str" em "int"
print(float('1') + 1) # o resultado deve ser = a 2.0 pois o "int" doi convertido para "float"
print(bool('')) # O resultado deve ser = "False" pois o espaço esta vazio
print(bool('com informação')) # O resultado deve ser = "True" pois o espaço foi preenchido
print(str(11) + 'b') # o resultado deve ser = "11b" pois o "int" foi convertido em "str"
