class Mision():
    def __init__(self, nombre: str, rango: int, recompensa: int, es_grupal: bool, min_miembros: int = 1):
        self.__nombre = nombre
        self.__rango = rango
        self.__recompensa = recompensa
        self.__es_grupal = es_grupal
        self.__min_miembros = min_miembros if es_grupal else 1
        self.__completada = False

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def rango(self):
        return self.__rango

    @rango.setter
    def rango(self, value):
        self.__rango = value

    @property
    def recompensa(self):
        return self.__recompensa

    @recompensa.setter
    def recompensa(self, value):
        self.__recompensa = value

    @property
    def es_grupal(self):
        return self.__es_grupal

    @es_grupal.setter
    def es_grupal(self, value):
        self.__es_grupal = value

    @property
    def min_miembros(self):
        return self.__min_miembros

    @min_miembros.setter
    def min_miembros(self, value):
        self.__min_miembros = value

    @property
    def completada(self):
        return self.__completada

    @completada.setter
    def completada(self, value):
        self.__completada = value