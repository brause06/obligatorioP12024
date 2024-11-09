class Mascota:
    def __init__(self, nombre: str, puntos_habilidad: int):
        self._nombre = nombre
        self._puntos_habilidad = puntos_habilidad

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def puntos_habilidad(self):
        return self._puntos_habilidad
    
    @puntos_habilidad.setter
    def puntos_habilidad(self, value):
        if not(1 <= value <= 50):
            raise ValueError("Los puntos de habilidad deben estar entre 1 y 50")
        self._puntos_habilidad = value