class Mision:
    def __init__(self, nombre: str, ranking: int, recompensa: int, es_grupal: bool, min_miembros: int = 1):
        self._nombre = nombre
        self._ranking = ranking
        self._recompensa = recompensa
        self._es_grupal = es_grupal
        self._min_miembros = min_miembros if es_grupal else 1
        self._completada = False

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def ranking(self):
        return self._ranking

    @ranking.setter
    def ranking(self, value):
        self._ranking = value

    @property
    def recompensa(self):
        return self._recompensa

    @recompensa.setter
    def recompensa(self, value):
        self._recompensa = value

    @property
    def es_grupal(self):
        return self._es_grupal

    @es_grupal.setter
    def es_grupal(self, value):
        self.__es_grupal = value

    @property
    def min_miembros(self):
        return self._min_miembros

    @min_miembros.setter
    def min_miembros(self, value):
        self._min_miembros = value

    @property
    def completada(self):
        return self._completada

    @completada.setter
    def completada(self, value):
        self._completada = value
