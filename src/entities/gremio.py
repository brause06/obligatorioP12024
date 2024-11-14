from typing import Dict, List

from entities.aventurero import Aventurero
from entities.mision import Mision

class Gremio():
    def __init__(self):
        self.__aventureros: Dict[int, Aventurero] = {}
        self.__misiones: Dict[str, Mision] = {}
    
    @property
    def aventureros(self):
        return self.__aventureros

    @property
    def misiones(self):
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

    def completar_mision(self, nombre: str, aventureros_ids: List[int]) -> bool:
        mision = self.buscar_mision(nombre)
        if not mision or mision.completada:
            return False
        aventureros = [self.buscar_aventurero(id) for id in aventureros_ids]

        if None in aventureros:
            return False
        
        return mision.completar_mision(aventureros)
    
    def top_aventureros_mayor_habilidad(self, limite: int = 10) -> List[Aventurero]:
        aventureros_ordenados = sorted(self.__aventureros.values(), key=lambda x: (x.calcular_habilidad_total(), x.nombre), reverse=True)
        return aventureros_ordenados[:limite]
    
    def top_misiones_mayor_recompensa(self, limite: int = 5) -> List[Mision]:
        misiones_ordenadas = sorted(self.__misiones.values(), key=lambda x: (x.recompensa, x.nombre), reverse=True)
        return misiones_ordenadas[:limite]
