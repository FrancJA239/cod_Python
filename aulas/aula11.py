#Precedências

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
# A operações são realizadas na ordem de precedências

#conta exemplo
# conta_1 = 1 + 1 ** 5 + 5 -> o resultado será = "7". Neste caso o resultado está incorreto
#Para o resultado esperado correto, terá que incluir "()" para priorizar a precedência

#exemplo prático
conta_2 = (1 + 1) ** (5 + 5)
print(conta_2)

# Curiosidade: Sempre que houver "()" dentro de "()", será priorizado de dentro para fora
# exemplo -> conta_3 = (7 + int(0.5 + 0.5)) ** (5 + 5) -> a operação int(5 + 5) será resolvida primeiro

#exemplo prático
conta_4 =  (7 + int(0.5 + 0.5)) ** (4 + 6)