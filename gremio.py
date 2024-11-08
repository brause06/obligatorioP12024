class Gremio():
    def __init__(self):
        self.__aventureros = []
        self.__misiones = []
    
    @property
    def aventureros(self):
        return self.__aventureros

    @aventureros.setter
    def aventureros(self, nuevo_aventurero):
        self.__aventureros = nuevo_aventurero

    @property
    def misiones(self, nueva_mision):
        self.__misiones = nueva_mision

            
