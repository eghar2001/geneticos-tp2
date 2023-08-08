from datos import objetos_volumen as objetos,VOLUMEN_MAXIMO

#EJERCICIO 2
mochila = []
objetos_ordenados = sorted(objetos, key= lambda obj:obj.valor / obj.volumen , reverse=True)

for obj in objetos_ordenados:
    total_volumen_mochila = sum(obj.volumen for obj in mochila)

    if total_volumen_mochila + obj.volumen < VOLUMEN_MAXIMO:
        mochila.append(obj)


valor_mochila = sum(obj.valor for obj in mochila)
volumen_mochila = sum(obj.volumen for obj in mochila)
print(f"mochila:{mochila} -- valor: {valor_mochila} -- volumen: {volumen_mochila}")

