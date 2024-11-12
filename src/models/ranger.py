from src.models.aventurero import Aventurero
from src.models.mascota import Mascota


class Ranger(Aventurero):
    def __init__(self, nombre: str, id: int, puntos_habilidad: int, experiencia: int, dinero: float):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.__mascota: Mascota = None
    
    @property
    def mascota(self) -> Mascota:
        return self.__mascota
    
    @mascota.setter
    def mascota(self, mascota: Mascota):
        self.__mascota = mascota