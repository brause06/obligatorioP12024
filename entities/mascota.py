class Mascota():
    def __init__(self, nombre: str, puntos_habilidad: int):
        self.__nombre = nombre
        self.__puntos_habilidad = puntos_habilidad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def puntos_habilidad(self):
        return self.puntos_habilidad
    
    