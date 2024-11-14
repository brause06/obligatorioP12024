from abc import ABC, abstractmethod
from typing import List

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from entities.mision import Mision

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

    @abstractmethod
    def calcular_rango(self) -> int:
        pass

    @abstractmethod
    def calcular_habilidad_total(self) -> int:
        pass
    
    def agregar_mision_completada(self, mision: 'Mision'):
        self.__misiones_completadas.append(mision)

    def agregar_dinero(self, dinero: float):
        self.dinero += dinero

    def agregar_experiencia(self, experiencia: int):
        self.experiencia += experiencia

    @property
    def misiones_completadas(self) -> List['Mision']:
        return self.__misiones_completadas
