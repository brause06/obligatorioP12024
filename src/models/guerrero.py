from obligatorioP12024.src.models.aventurero import Aventurero


class Guerrero(Aventurero):
    def __init__(self, nombre: str, id: int, puntos_habilidad: int, experiencia: int, dinero: float, fuerza: int):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self._fuerza = fuerza

    @property
    def fuerza(self):
        return self._fuerza

    @fuerza.setter
    def fuerza(self, value):
        self._fuerza = value