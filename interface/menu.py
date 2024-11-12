from entities.gremio import Gremio
from entities.guerrero import Guerrero
from entities.mago import Mago
from entities.ranger import Ranger
from entities.mascota import Mascota
from entities.mision import Mision

from typing import List

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
                if min_value <= user_input <= max_value:
                    return user_input
                print("Valor invalido")
            except ValueError:
                print("Valor invalido")

    def get_valid_float(self, prompt: str, min_value: float):
        while True:
            try:
                user_input = float(input(prompt))
                if user_input >= min_value: 
                    return user_input
                print("Valor invalido")
            except ValueError:
                print("Valor invalido")

    def registrar_aventurero(self):
        print("\nRegistrar Aventurero\n")
        
        # 1. Elegir la clase del aventurero
        print("Elija la clase de aventurero:")
        print("1 - Guerrero")
        print("2 - Mago")
        print("3 - Ranger")
        
        opcion_clase = self.get_valid_input("Ingrese el número de la clase (1-3): ", ["1", "2", "3"])
            
        while True:
            id_unico = self.get_valid_int("Ingrese un ID único: ", 1, 10000)
            if not self.gremio.buscar_aventurero(id_unico):  
                break
            print("Error: Ya existe un aventurero con este ID. Intente nuevamente.")

        nombre = input("Ingrese el nombre del aventurero: ")
        puntos_habilidad = self.get_valid_int("Ingrese puntos de habilidad (0-100): ", 0, 100)
        experiencia = self.get_valid_int("Ingrese experiencia: ", 0, 1000)
        dinero = self.get_valid_float("Ingrese cantidad de dinero: ", 0.0)
   
            #Creo el aventurero según la opción elegida
        if opcion_clase == "1":
            fuerza = self.get_valid_int("Ingrese fuerza (0-100): ", 0, 100)
            aventurero = Guerrero(nombre, id_unico, puntos_habilidad, experiencia, dinero, fuerza)
        elif opcion_clase == "2":
            mana = self.get_valid_int("Ingrese mana (0-1000): ", 0, 1000)
            aventurero = Mago(nombre, id_unico, puntos_habilidad, experiencia, dinero, mana)
        elif opcion_clase == "3":
            tiene_mascota = self.get_valid_input("¿El ranger tiene mascota? (s/n): ", ["s", "n"])
            mascota = None
            if tiene_mascota == "s":
                nombre_mascota = input("Ingrese el nombre de la mascota: ")
                puntos_habilidad_mascota = self.get_valid_int("Ingrese puntos de habilidad de la mascota (1-50): ", 1, 50)
                mascota = Mascota(nombre_mascota, puntos_habilidad_mascota)
            aventurero = Ranger(nombre, id_unico, puntos_habilidad, experiencia, dinero, mascota)
        
        if self.gremio.agregar_aventurero(aventurero):
            print("\nAventurero registrado exitosamente!\n")
        else:
            print("Error: No se pudo registrar al aventurero.")

            
    def registrar_mision(self):
        print("\nRegistrar Misión\n")
        
        nombre = input("Ingrese el nombre de la misión: ")
        rango_mision = self.get_valid_int("Ingrese el rango de la misión (1-5): ", 1, 5)
        recompensa = self.get_valid_float("Ingrese la recompensa de la misión: ", 0.0)
        es_grupal = self.get_valid_input("¿Es una misión grupal? (s/n): ", ["s", "n"]) == "s"
        min_miembros = 1 

        if es_grupal:
            min_miembros = self.get_valid_int("Ingrese la cantidad de miembros: ", 1, 100)
        try:
            mision = Mision(nombre=nombre, rango=rango_mision, recompensa=recompensa, es_grupal=es_grupal, min_miembros=min_miembros)
            if self.gremio.agregar_mision(mision):
                print("\n Misión registrada exitosamente!\n")
            else:
                print("\nYa existe una misión con el mismo nombre.\n")
        except ValueError as e:
            print(f"\nError al registrar la misión: {e}")


    def realizar_mision(self):
        print("Realizar Misión")
        
        id_aventurero = self.get_valid_int("Ingrese el ID del aventurero: ", 1, 10000)
        nombre_mision = input("Ingrese el nombre de la misión: ")
        
        aventurero = self.gremio.buscar_aventurero(id_aventurero)
        mision = self.gremio.buscar_mision(nombre_mision)
        
        if aventurero and mision:
            # Aquí podrías agregar lógica de dificultad, recompensas, etc.
            print(f"El aventurero {aventurero.nombre} ha completado la misión {mision.nombre}.")
            # Quizás actualizar experiencia, dinero, o habilidades aquí
        else:
            print("Error: Aventurero o misión no encontrados.")

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