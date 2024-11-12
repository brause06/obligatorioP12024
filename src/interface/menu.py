from obligatorioP12024.src.models.gremio import Gremio
from obligatorioP12024.src.models.guerrero import Guerrero
from obligatorioP12024.src.models.mago import Mago
from obligatorioP12024.src.models.mascota import Mascota
from obligatorioP12024.src.models.ranger import Ranger


class Menu:
    def __init__(self):
        self.gremio = Gremio()    

    def display_menu(self):
        print("Seleccione una opcion:")  
        print("1. Registrar aventurero")
        print("2. Registrar mision")
        print("3. Realizar mision")
        print("4. Otras consultas")
        print("5. Salir")

    def get_valid_input(self, prompt: str, opciones_validas: List[str]):
        while True:
            user_input = input(prompt)
            if user_input in opciones_validas:
                return user_input
            print("Opcion invalida")

    def get_valid_int(self, prompt: str, min_value: int, max_value: int):
        while True:
            try:
                user_input = int(input(prompt))
                if min_value < user_input < max_value:
                    return user_input
                print("Valor invalido")
            except ValueError:
                print("Valor invalido")

    def get_valid_float(self, prompt: str, min_value: float):
        while True:
            try:
                user_input = float(input(prompt))
                if min_value < user_input :
                    return user_input
                print("Valor invalido")
            except ValueError:
                print("Valor invalido")
            

    def registrar_aventurero(self):
        print("\nRegistro de Aventurero")
        print("Elija la clase del aventurero:")
        print("1. Guerrero")
        print("2. Mago")
        print("3. Ranger")

        class_opcion = self.get_valid_input("Seleccione una opcion (1-3): ", ["1", "2", "3"])

        try:
            name = input("Ingrese el nombre: ")
            if not name:
                print("El nombre no puede estar vacio")
                return
            
            id = self.get_valid_int("Ingrese el id del aventurero: ", 0, 10000)
            if id in self.gremio.aventureros:
                print("Ya existe un aventurero con ese id")
                return
            
            puntos_habilidad = self.get_valid_int("Ingrese los puntos de habilidad (1-100): ", 1, 100)
            experiencia = self.get_valid_int("Ingrese la experiencia: ", 0, 100000)
            dinero = self.get_valid_float("Ingrese el dinero: ", 0.0)

            #CREAR AVENTURERO
            aventurero = None
            if class_opcion == 1: # Guerrero
                fuerza = self.get_valid_int("Ingrese la fuerza (1-100): ", 1, 100)
                aventurero = Guerrero(name, id, puntos_habilidad, experiencia, dinero, fuerza)

            elif class_opcion == "2": #Mago
                mana = self.get_valid_int("Ingrese el mana (1-1000): ", 1, 1000)
                aventurero = Mago(name, id, puntos_habilidad, experiencia, dinero, mana)

            else: # Ranger
                aventurero = Ranger(name, id, puntos_habilidad, experiencia, dinero)
                tiene_mascota = self.get_valid_input("El aventurero tiene mascota? (s/n): ", ["s", "n"])
                if tiene_mascota == "s":
                    nombre_mascota = input("Ingrese el nombre de la mascota: ")
                    if not nombre_mascota:
                        print("El nombre de la mascota no puede estar vacio")
                        return
                    habilidad_mascota = self.get_valid_int("Ingrese la habilidad de la mascota (1-50): ", 1, 50)
                    aventurero.mascota(Mascota(nombre_mascota, habilidad_mascota))

            if self.gremio.agregar_aventurero(aventurero):
                print("Aventurero registrado con exito")
            else:
                print("Error al registrar el aventurero")
            
        except ValueError as e:
            print(f"Error: {str(e)}")

    def registrar_mision(self):
        pass

    def realizar_mision(self):
        pass

    def run(self):
        while True:
            self.display_menu()
            opcion = self.get_valid_input("Ingrese la opcion deseada: ", ["1", "2", "3", "4", "5"])
            if opcion == "1":
                self.registrar_aventurero()
            elif opcion == "2":
                self.registrar_mision()
            elif opcion == "3":
                self.realizar_mision()
            elif opcion == "4":
                pass
            elif opcion == "5":
                break