from entities.aventurero import Aventurero
from entities.mascota import Mascota

class Ranger(Aventurero):
    def __init__(self, nombre: str, id: int, puntos_habilidad: int, experiencia: int, dinero: float, mascota: Mascota = None):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.__mascota = mascota

    @property
    def mascota(self):
        return self.__mascota
    
        