from itertools import combinations

from datos import objetos_peso as objetos, PESO_MAXIMO

#parte I- busqueda exhaustiva
combinaciones: [] = []
for r in range(1, len(objetos) + 1):
    for comb in combinations(objetos, r):
        peso_total = sum(obj.peso for obj in comb)
        if peso_total <= PESO_MAXIMO:
            combinaciones.append(comb)

valor_max = 0
comb_max = combinaciones[0]
for comb in combinaciones:
    valor_total = sum(obj.valor for obj in comb)
    if valor_total > valor_max:
        valor_max = valor_total
        comb_max = comb

peso = sum(obj.peso for obj in comb_max)
print("BUSQUEDA EXHAUSTIVA")
print(f"combinacion maxima: {comb_max} -- valor: {valor_max} -- peso: {peso}\n")



#parte II- busqueda golosa
mochila = []
objetos_ordenados = sorted(objetos, key= lambda obj:obj.valor/obj.peso , reverse=True)

for obj in objetos_ordenados:
    total_peso_mochila = sum(obj.peso for obj in mochila)

    if total_peso_mochila + obj.peso < PESO_MAXIMO:
        mochila.append(obj)


valor_mochila = sum(obj.valor for obj in mochila)
peso_mochila = sum(obj.peso for obj in mochila)
print("BUSQUEDA GOLOSA")
print(f"mochila:{mochila} -- valor: {valor_mochila} -- peso: {valor_mochila}")