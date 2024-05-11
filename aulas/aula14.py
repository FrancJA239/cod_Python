a = 'A'
b = 'B'
x1 = 1.1
formato = 'a={} b={} c={}'.format(a, b, x1)
# Neste caso estou incluindo "{}" em meio ao "texto" para posteriormente usar ".format" com variáveis dentro de "()"
# ao printar "formato" o resultado será "a=A b=B c=1.1"
print(formato)

c = 'CCC'
d = 'DDD'
x5 = 5.55
formato_2 = 'x={1} x={0} c={:.2f}'.format(c, d, x5)
print(formato_2)
# dentro das "{}" eu também posso formatar o meu argumento que será apresentado
# Posso também mudar a ordem dos argumento da seguinte forma "{1}" e depois "{3}"


# parametro nomeado
f = 'CCC'
g = 'DDD'
h = 'HHH'
string = 'x={nomef} x={nomeh} c={nomeg}' # desta forma que consigo nomear e organizar melhor a minha linha de cod
formato_2 = string.format(
    nomef=f, nomeg=g, nomeh=h,
)
# Neste formato, eu inclui um "nome" para o meu argumento
# essa pratica é chamada de "Parametro nomeado"
# Após nomear um poaratro, todos em seguida devem ser nomeados também
print(formato_2)