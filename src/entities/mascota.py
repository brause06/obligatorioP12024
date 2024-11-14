class Mascota:
    def __init__(self, nombre: str, puntos_habilidad: int):
        self.__nombre = nombre
        self.__puntos_habilidad = puntos_habilidad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad
    
    @puntos_habilidad.setter
    def puntos_habilidad(self, value):
        if not(1 <= value <= 50):
            raise ValueError("Los puntos de habilidad deben estar entre 1 y 50")
        self.__puntos_habilidad = value