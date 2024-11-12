from typing import Dict

from obligatorioP12024.src.models.aventurero import Aventurero
from obligatorioP12024.src.models.mision import Mision

class Gremio:
    def __init__(self):
        self.__aventureros: Dict[int, Aventurero] = {}
        self.__misiones: Dict[str, Mision] = {}

    @property
    def aventureros(self) -> Dict[int, Aventurero]:
        return self.__aventureros


    @property
    def misiones(self) -> Dict[str, Mision]:
        return self.__misiones

def agregar_aventurero(self, aventurero: Aventurero) -> bool:
    if aventurero.id in self.__aventureros:
        return False
    self.__aventureros[aventurero.id] = aventurero
    return True

def agregar_mision(self, mision: Mision) -> bool:
    if mision.nombre in self.__misiones:
        return False
    self.__misiones[mision.nombre] = mision
    return True

def buscar_aventurero(self, id: int) -> Aventurero:
    return self.__aventureros.get(id)

def buscar_mision(self, nombre: str) -> Mision:
    return self.__misiones.get(nombre)


