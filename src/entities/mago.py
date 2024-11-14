from entities.aventurero import Aventurero

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
    