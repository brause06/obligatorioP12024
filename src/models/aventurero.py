from abc import ABC


class Aventurero(ABC):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero):
        self.nombre = nombre
        self.id = id
        self.puntos_habilidad = puntos_habilidad
        self.experiencia = experiencia
        self.dinero = dinero




class Guerrero(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, fuerza):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.fuerza = fuerza



class Mago(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, mana):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.mana = mana


class Ranger(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero)
        self.mascota: Mascota = None

class Mascota:
    def __init__(self, nombre, puntos_habilidad):
        self.nombre = nombre
        self.puntos_habilidad = puntos_habilidad
