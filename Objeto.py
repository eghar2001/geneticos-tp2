from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Objeto:
    _last_id:ClassVar[int] = 0

    _id:int
    _volumen:int
    _peso: int
    _valor:int


    def __init__(self, volumen:int = 0, peso:int = 0, valor:int = 0):
        self._id = self.asigna_id()
        self.volumen = volumen
        self.valor = valor
        self.peso = peso

    @property
    def id(self):
        return self._id

    @property
    def volumen(self): #cm3
        """Volumen del objeto en cm3"""
        return self._volumen

    @property
    def peso(self):  # gramos
        """Peso del objeto en gramos"""
        return self._peso

    @property
    def valor(self):#pesos
        """Valor del objeto en pesos"""
        return self._valor



    @volumen.setter
    def volumen(self, volumen): #cm3
        """Volumen del objeto en cm3"""
        if volumen >= 0:
            self._volumen = volumen
        else:
            raise ValueError("El volumen ingresado es incorrecto")

    @peso.setter
    def peso(self, peso):#gramos
        if peso>= 0:
            self._peso = peso
        else:
            raise ValueError("El peso ingresado es incorrecto")

    @valor.setter
    def valor(self,valor):
        """Valor del objeto en pesos"""
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("El valor ingresado es incorrecto")

    def __str__(self):
        return f"Objeto<id:{self.id} -- valor: {self.valor} -- volumen: {self.volumen}>"

    def __repr__(self):
        return f"Objeto<id:{self.id} -- valor: {self.valor} -- volumen: {self.volumen}>"

    def get_proporcion(self):
        return self.valor / self.volumen

    @classmethod
    def asigna_id(cls):
        cls._last_id +=1
        return cls._last_id