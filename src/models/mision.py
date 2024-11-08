class Mision:
    def __init__(self, nombre: str, ranking: int, recompensa: int, es_grupal: bool, min_miembros: int = 1):
        self.nombre = nombre
        self.ranking = ranking
        self.recompensa = recompensa
        self.es_grupal = es_grupal
        self.min_miembros = min_miembros if es_grupal else 1
        self.completada = False
