from dataclasses import dataclass
from itertools import combinations

VOLUMEN_MAXIMO:int = 4200
@dataclass
class Objeto:

    _volumen:int
    _valor:int

    @property
    def volumen(self):
        return self._volumen

    @property
    def valor(self):
        return self._valor

    @volumen.setter
    def volumen(self, volumen):
        self._volumen = volumen


    @valor.setter
    def valor(self,valor):
        self._valor = valor

    def __str__(self):
        return f"Objeto<valor: {self.valor} -- volumen: {self.volumen}>"

    def get_proporcion(self):
        return self.valor / self.volumen


objetos = [
   Objeto(150,20),
   Objeto(325,40),
   Objeto(600,50),
   Objeto(805,36),
   Objeto(430,25),
   Objeto(1200,64),
   Objeto(779, 54),
   Objeto(60, 18),
   Objeto(930, 46),
   Objeto(358, 28),
]



#PARTE 1

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



#PARTE 2
mochila = []
objetos_ordenados = sorted(objetos, key= lambda obj:obj.get_proporcion() , reverse=True)

for obj in objetos_ordenados:
    total_volumen_mochila = sum(obj.volumen for obj in mochila)

    if total_volumen_mochila + obj.volumen < VOLUMEN_MAXIMO:
        mochila.append(obj)


valor_mochila = sum(obj.valor for obj in mochila)
volumen_mochila = sum(obj.volumen for obj in mochila)
print(f"mochila:{mochila} -- valor: {valor_mochila} -- volumen: {volumen_mochila}")


# PARTE 3
@dataclass
class Objeto:
    _peso: int
    _valor: int

    @property
    def peso(self):
        return self._peso

    @property
    def valor(self):
        return self._valor

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    def __str__(self):
        return f"Objeto<valor: {self.valor} -- volumen: {self._peso}>"


objetos = [
    Objeto(1800, 72),
    Objeto(600, 36),
    Objeto(1200, 60)

]

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


