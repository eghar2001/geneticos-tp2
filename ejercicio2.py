from datos import objetos_volumen as objetos,VOLUMEN_MAXIMO
from time import perf_counter

#EJERCICIO 2
tiempo_inicio = perf_counter()
mochila = []
objetos_ordenados = sorted(objetos, key= lambda obj:obj.valor / obj.volumen , reverse=True)

for obj in objetos_ordenados:
    total_volumen_mochila = sum(obj.volumen for obj in mochila)

    if total_volumen_mochila + obj.volumen < VOLUMEN_MAXIMO:
        mochila.append(obj)
tiempo_fin = perf_counter()
duracion = tiempo_fin - tiempo_inicio

valor_mochila = sum(obj.valor for obj in mochila)
volumen_mochila = sum(obj.volumen for obj in mochila)
print(f"mochila:{mochila} --\n valor: {valor_mochila} --\n volumen: {volumen_mochila} -- \n tiempo demorado: {duracion}")

