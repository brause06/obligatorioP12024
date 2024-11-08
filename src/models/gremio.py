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

    @aventureros.setter
    def aventureros(self, aventureros: Dict[int, Aventurero]):
        self._aventureros = aventureros

    @property
    def misiones(self) -> Dict[str, Mision]:
        return self._misiones

    @misiones.setter
    def misiones(self, misiones: Dict[str, Mision]):
        self._misiones = misiones
