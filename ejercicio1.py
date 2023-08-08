
from itertools import combinations
from datos import objetos_volumen as objetos,VOLUMEN_MAXIMO



#Declaracion de los objetos usados en la parte I Y II




#EJERCICIO 1
"""Resolver el problema de la Mochila utilizando una búsqueda exhaustiva"""
combinaciones:[] = []
for r in range(1, len(objetos) + 1):
    for comb in combinations(objetos, r):
        volumen_total = sum(obj.volumen for obj in comb)
        if volumen_total <= VOLUMEN_MAXIMO:
            combinaciones.append(comb)


valor_max = 0
comb_max = combinaciones[0]
for comb in combinaciones:
    valor_total = sum(obj.valor for obj in comb)
    if valor_total > valor_max:
        valor_max=valor_total
        comb_max =  comb

volumen = sum(obj.volumen for obj in comb_max)

print(f"combinacion maxima: {comb_max} -- valor: {valor_max} -- volumen: {volumen}")



"""
# PARTE 3


"""

