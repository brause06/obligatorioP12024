from typing import Dict

from obligatorioP12024.src.models.aventurero import Aventurero
from obligatorioP12024.src.models.mision import Mision

class Gremio:
    def __init__(self):
        self.aventureros: Dict[int, Aventurero] = {}
        self.misiones = Dict[str, Mision] = {}
