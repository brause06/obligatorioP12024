from typing import Dict

from obligatorioP12024.src.models.aventurero import Aventurero
from obligatorioP12024.src.models.mision import Mision

class Gremio:
    def __init__(self):
        self._aventureros: Dict[int, Aventurero] = {}
        self._misiones: Dict[str, Mision] = {}

    @property
    def aventureros(self) -> Dict[int, Aventurero]:
        return self._aventureros


    @property
    def misiones(self) -> Dict[str, Mision]:
        return self._misiones

def agregar_aventurero(self, aventurero: Aventurero) -> bool:
    if aventurero.id in self._aventureros:
        return False
    self._aventureros[aventurero.id] = aventurero
    return True

def agregar_mision(self, mision: Mision) -> bool:
    if mision.nombre in self._misiones:
        return False
    self._misiones[mision.nombre] = mision
    return True

def buscar_aventurero(self, id: int) -> Aventurero:
    return self._aventureros.get(id)

def buscar_mision(self, nombre: str) -> Mision:
    return self._misiones.get(nombre)


