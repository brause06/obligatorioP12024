from abc import ABC


class Aventurero(ABC):
    def __init__(self, nombre: str, id: int, puntos_habilidad: int, experiencia: int, dinero: float):
        self._nombre = nombre
        self._id = id
        self._puntos_habilidad = puntos_habilidad
        self._experiencia = experiencia
        self._dinero = dinero

        @property
        def nombre(self):
            return self._nombre

        @nombre.setter
        def nombre(self, value):
            self._nombre = value

        @property
        def id(self):
            return self._id

        @id.setter
        def id(self, value):
            self._id = value

        @property
        def puntos_habilidad(self):
            return self._puntos_habilidad

        @puntos_habilidad.setter
        def puntos_habilidad(self, value):
            self._puntos_habilidad = value

        @property
        def experiencia(self):
            return self._experiencia

        @experiencia.setter
        def experiencia(self, value):
            self._experiencia = value

        @property
        def dinero(self):
            return self._dinero

        @dinero.setter
        def dinero(self, value):
            self._dinero = value
