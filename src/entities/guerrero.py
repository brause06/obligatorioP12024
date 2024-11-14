from src.entities.aventurero import Aventurero


class Guerrero(Aventurero):
    def __init__(self, nombre: str, id: int, puntos_habilidad: int, experiencia: int, dinero: float, fuerza: int):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.__fuerza = fuerza

    @property
    def fuerza(self):
        return self.__fuerza

    @fuerza.setter
    def fuerza(self, value):
        if not(1 <= value <= 100):
            raise ValueError("La fuerza debe estar entre 1 y 100")
        self.__fuerza = value

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
        return self.puntos_habilidad + self.fuerza / 2
