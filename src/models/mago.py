from obligatorioP12024.src.models.aventurero import Aventurero


class Mago(Aventurero):
    def __init__(self, nombre: str, id: int, puntos_habilidad: int, experiencia: int, dinero: float, mana: int):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self._mana = mana

    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, value):
        self._mana = value
