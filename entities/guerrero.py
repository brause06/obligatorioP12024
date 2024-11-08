from entities.aventurero import Aventurero

class Guerrero(Aventurero):
    def __init__(self, nombre: str, id: int, puntos_habilidad: int, experiencia: int, dinero: float, fuerza: int):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.__fuerza = fuerza

    @property
    def fuerza(self):
        return self.__fuerza
    
