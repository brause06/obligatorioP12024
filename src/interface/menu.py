from src.models.gremio import Gremio
from src.models.guerrero import Guerrero
from src.models.mago import Mago
from src.models.mascota import Mascota
from src.models.mision import Mision
from src.models.ranger import Ranger
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

    def otras_consultas_menu(self):

        while True:
            print("\nOtras Consultas:")
            print("1. Ver Top 10 Aventureros con Más Misiones Resueltas")
            print("2. Ver Top 10 Aventureros con Mayor Habilidad")
            print("3. Ver Top 5 Misiones con Mayor Recompensa")
            print("4. Volver al menu principal")
            print("5. Salir")

            opcion = self.get_valid_input("Ingrese la opcion deseada: ", ["1", "2", "3", "4", "5"])

            if opcion == "1":
                self.top_aventureros_mas_misiones_resueltas()
            elif opcion == "2":
                self.top_aventureros_mayor_habilidad()
            elif opcion == "3":
                self.top_misiones_mayor_recompensa()
            else:
                break

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
        print(class_opcion)
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
            if class_opcion == "1": # Guerrero
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
        print("Registro de mision")

        try:
            nombre = input("Ingrese el nombre de la mision: ")
            if not nombre:
                print("El nombre no puede estar vacio")
                return
            
            if nombre in self.gremio.misiones:
                print("Ya existe una mision con ese nombre")
                return

            ranking = self.get_valid_int("Ingrese el ranking de la mision (1-5): ", 1, 5)
            recompensa = self.get_valid_float("Ingrese la recompensa de la mision: ", 0)
            es_grupal = self.get_valid_input("La mision es grupal? (s/n): ", ["s", "n"]) == "s"
            min_miembros = 1
            if es_grupal:
                min_miembros = self.get_valid_int("Ingrese la cantidad minima de miembros (2-10): ", 2, 10)

            mision = Mision(nombre, ranking, recompensa, es_grupal, min_miembros)
            if self.gremio.agregar_mision(mision):
                print("Mision registradado correctamente")
            else:
                print("Error al registrar la mision")
        

        except ValueError as e:
            print(f"Error: {str(e)}")

    def realizar_mision(self):
        print("ealizar mision")

        nombre_mision = input("Ingrese el nombre de la mision: ")
        mision = self.gremio.buscar_mision(nombre_mision)

        if not mision:
            print("Mision no encontrada")
            return
        
        if mision.completada:
            print("La mision ya fue completada")
            return
        
        aventureros_ids = []
        while True:
            try:
                id_aventurero = self.get_valid_int("Ingrese el id del aventurero: ", 0, 10000)
                aventurero = self.gremio.buscar_aventurero(id_aventurero)

                if not aventurero:
                    print("Aventurero no encontrado")
                    continue
                if id_aventurero in aventureros_ids:
                    print("Aventurero ya registrado")
                    continue

                aventureros_ids.append(id_aventurero)

                if len(aventureros_ids) >= mision.min_miembros:
                    siguiente = self.get_valid_input("Desea agregar otro aventurero? (s/n): ", ["s", "n"])
                    if siguiente == "n":
                        break

            

            except ValueError as e:
                print(f"Error: {str(e)}")
                return
            
            if self.gremio.completar_mision(nombre_mision, aventureros_ids):
                print("Mision completada con exito")
            else:
                print("Error al completar la mision")



    def top_aventureros_mas_misiones_resueltas(self):
        pass

    def top_aventureros_mayor_habilidad(self):
        pass

    def top_misiones_mayor_recompensa(self):
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
                self.otras_consultas_menu()
            elif opcion == "5":
                break