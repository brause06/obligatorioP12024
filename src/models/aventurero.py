from abc import ABC


class Aventurero(ABC):
    def __init__(self, nombre: str, id: int, puntos_habilidad: int, experiencia: int, dinero: float):
        self.__nombre = nombre
        self.__id = id
        self.__puntos_habilidad = puntos_habilidad
        self.__experiencia = experiencia
        self.__dinero = dinero

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad

    @puntos_habilidad.setter
    def puntos_habilidad(self, value):
        if not(1 <= value <= 100):
            raise ValueError("Los puntos de habilidad deben estar entre 1 y 100")
        self.__puntos_habilidad = value

    @property
    def experiencia(self):
        return self.__experiencia

    @experiencia.setter
    def experiencia(self, value):
        self.__experiencia = value

    @property
    def dinero(self):
        return self.__dinero

    @dinero.setter
    def dinero(self, value):
        self.__dinero = value
