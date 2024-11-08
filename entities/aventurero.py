from abc import ABC

class Aventurero(ABC):
    def __init__(self, nombre: str, id: int, puntos_habilidad: int, experiencia: int, dinero: float):
        self.__nombre = nombre
        self.__id = id
        self.__puntos_habilidad = puntos_habilidad
        self.__experiencia = experiencia
        self.__dinero = dinero
        self.__misiones_completadas = []

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def id(self):
        return self.__id
    
    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad
    
    @puntos_habilidad.setter
    def puntos_habilidad(self, nuevo_puntos):
        self.__puntos_habilidad = nuevo_puntos
    
    @property
    def experiencia(self):
        return self.__experiencia
    
    @experiencia.setter
    def experiencia(self, nuevo_experiencia):
        self.__experiencia = nuevo_experiencia    
    
    @property
    def dinero(self):
        return self.__dinero
    
    @dinero.setter
    def dinero(self, nuevo_dinero):
        self.__dinero = nuevo_dinero

    @property
    def misiones_completadas(self):
        return self.__misiones_completadas
    
    def __eq__(self, otro_aventurero):
        return self.id == otro_aventurero.id
    