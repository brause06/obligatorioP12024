from src.entities.aventurero import Aventurero


class Mago(Aventurero):
    def __init__(self, nombre: str, id: int, puntos_habilidad: int, experiencia: int, dinero: float, mana: int):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.__mana = mana

    @property
    def mana(self):
        return self.__mana
    
    @mana.setter
    def mana(self, value):
        if not(1 <= value <= 1000):
            raise ValueError("El mana debe estar entre 1 y 1000")
        self.__mana = value

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
        return self.puntos_habilidad + self.mana / 10