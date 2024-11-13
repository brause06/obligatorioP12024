from typing import List

from src.models.aventurero import Aventurero


class Mision:
    def __init__(self, nombre: str, ranking: int, recompensa: int, es_grupal: bool, min_miembros: int = 1):
        self.__nombre = nombre
        self.__ranking = ranking
        self.__recompensa = recompensa
        self.__es_grupal = es_grupal
        self.__min_miembros = min_miembros if es_grupal else 1
        self.__completada = False
        self.__participantes: List[Aventurero] = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def ranking(self):
        return self.__ranking

    @ranking.setter
    def ranking(self, value):
        self.__ranking = value

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
    
    @property
    def participantes(self):
        return self.__participantes
    
    @participantes.setter
    def participantes(self, value):
        self.__participantes = value


    

    def completar_mision(self, aventureros: List[Aventurero]) -> bool:
        if not self.puede_ser_completada(aventureros):
            return False
        self.completada(True)
        self.participantes(aventureros)

        #Calcula recompensa
        recompensa_por_participante = self.recompensa / len(aventureros)

        # Tabla de experiencia según el rango de la misión
        recompensa_experiencia = {
            1: 5,    # Misión rango 1: 5 puntos de experiencia
            2: 10,   # Misión rango 2: 10 puntos de experiencia
            3: 20,   # Misión rango 3: 20 puntos de experiencia
            4: 50,   # Misión rango 4: 50 puntos de experiencia
            5: 100   # Misión rango 5: 100 puntos de experiencia
        }
        experiencia = recompensa_experiencia[self.ranking]

        # Distribuye recompensas y experiencia a cada participante
        for aventurero in aventureros:
            aventurero.agregar_dinero(recompensa_por_participante)
            aventurero.agregar_experiencia(experiencia)
            aventurero.agregar_mision_completada(self)

        return True




    def puede_ser_completada(self, aventureros: List[Aventurero]) -> bool:
        if len(aventureros) < self.min_miembros:
            return False
        return all(aventurero.calcular_rango() >= self.ranking for aventurero in aventureros)