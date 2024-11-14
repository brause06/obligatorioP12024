from entities.aventurero import Aventurero
from entities.mascota import Mascota


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

    def calcular_rango(self) -> int:
        puntos_habilidad = self.calcular_habilidad_total()
        if puntos_habilidad > 80:
            return 5
        elif puntos_habilidad > 60:
            return 4
        elif puntos_habilidad > 40:
            return 3
        elif puntos_habilidad > 20:
            return 2
        else:
            return 1

    def calcular_habilidad_total(self) -> int:
        puntos_habilidad_base = self.puntos_habilidad
        if self.mascota and self.calcular_rango() <= 4:
            puntos_habilidad_base += self.mascota.puntos_habilidad
        return puntos_habilidad_base
