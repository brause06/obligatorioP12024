from obligatorioP12024.src.models.aventurero import Aventurero
from obligatorioP12024.src.models.mascota import Mascota


class Ranger(Aventurero):
    def __init__(self, nombre: str, id: int, puntos_habilidad: int, experiencia: int, dinero: float):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self._mascota: Mascota = None