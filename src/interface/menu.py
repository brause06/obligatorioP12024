from entities.gremio import Gremio
from entities.guerrero import Guerrero
from entities.mago import Mago
from entities.mascota import Mascota
from entities.mision import Mision
from entities.ranger import Ranger
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

    def display_submenu_consultas(self):
        print("\nConsultas:")
        print("1. Ver Top 10 Aventureros con Más Misiones Resueltas")
        print("2. Ver Top 10 Aventureros con Mayor Habilidad")
        print("3. Ver Top 5 Misiones con Mayor Recompensa")
        print("4. Volver al menú principal")

    def get_valid_input(self, prompt: str, opciones_validas: List[str]):
        try:
            user_input = input(prompt)
            if user_input in opciones_validas:
                return user_input
            print("Opción inválida.\n")
            return None
        except ValueError:
            print("Valor inválido.\n")
            return None

    def get_valid_int(self, prompt: str, min_value: int, max_value: int):
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input #si esta en el rango, me devuelve el valor
            print(f"Valor inválido. Debe ingresar un valor entre {min_value} y {max_value}.\n")
            return None  #si es invalido, me devuelve none
        except ValueError:
            print("Valor inválido.\n")
            return None

    def get_valid_float(self, prompt: str, min_value: float):
        try:
            user_input = float(input(prompt))
            if user_input >= min_value:
                return user_input
            print(f"Valor inválido. Debe ingresar un valor mayor o igual a {min_value}.\n")
            return None 
        except ValueError:
            print("Valor inválido.\n")
            return None  

    def registrar_aventurero(self):
        print("\nRegistrar Aventurero en el Gremio\n")
        print("Seleccione la clase de aventurero:")
        print("1 - Guerrero")
        print("2 - Mago")
        print("3 - Ranger")

        
        opcion_clase = self.get_valid_input("Ingrese el número de la clase (1-3): ", ["1", "2", "3"])
        if opcion_clase is None:
            return  # vuelvo al menú si la entrada no es valida 

        id_unico = self.get_valid_int("Ingrese un ID único: ", 1, 10000)
        if id_unico is None:
            return 
        if self.gremio.buscar_aventurero(id_unico):
            print("Ya existe un aventurero registrado con este ID. Intente nuevamente.")
            return

        nombre = input("Ingrese el nombre del aventurero: ")
        puntos_habilidad = self.get_valid_int("Ingrese puntos de habilidad (0-100): ", 0, 100)
        if puntos_habilidad is None:
            return 
        experiencia = self.get_valid_int("Ingrese experiencia (0-1000): ", 0, 1000)
        if experiencia is None:
            return 
        dinero = self.get_valid_float("Ingrese cantidad de dinero (>= 0): ", 0.0)
        if dinero is None:
            return 

        if opcion_clase == "1": 
            fuerza = self.get_valid_int("Ingrese fuerza (0-100): ", 0, 100)
            if fuerza is None:
                return 
            aventurero = Guerrero(nombre, id_unico, puntos_habilidad, experiencia, dinero, fuerza)
        elif opcion_clase == "2":  # Mago
            mana = self.get_valid_int("Ingrese mana (0-1000): ", 0, 1000)
            if mana is None:
                return 
            aventurero = Mago(nombre, id_unico, puntos_habilidad, experiencia, dinero, mana)
        elif opcion_clase == "3":  # Ranger
            tiene_mascota = self.get_valid_input("¿El ranger tiene mascota? (s/n): ", ["s", "n"])
            if tiene_mascota is None:
                return
            mascota = None
            if tiene_mascota == "s":
                nombre_mascota = input("Ingrese el nombre de la mascota: ")
                puntos_habilidad_mascota = self.get_valid_int("Ingrese puntos de habilidad de la mascota (1-50): ", 1, 50)
                if puntos_habilidad_mascota is None:
                    return  
                mascota = Mascota(nombre_mascota, puntos_habilidad_mascota)
            aventurero = Ranger(nombre, id_unico, puntos_habilidad, experiencia, dinero, mascota)

        #Agrega el aventurero al gremio si todo esta ok
        if self.gremio.agregar_aventurero(aventurero):
            print("\nAventurero registrado exitosamente!\n")

    def registrar_mision(self):
        print("\nRegistrar Misión\n")
        
        nombre = input("Ingrese el nombre de la misión: ")
        rango_mision = self.get_valid_int("Ingrese el rango de la misión (1-5): ", 1, 5)
        recompensa = self.get_valid_float("Ingrese la recompensa de la misión: ", 0.0)
        es_grupal = self.get_valid_input("¿Es una misión grupal? (s/n): ", ["s", "n"]) == "s"
        min_miembros = 1 

        if es_grupal:
            min_miembros = self.get_valid_int("Ingrese la cantidad mínima de miembros: ", 1, 100)
        
            mision = Mision(nombre=nombre, rango=rango_mision, recompensa=recompensa, es_grupal=es_grupal, min_miembros=min_miembros)
            if self.gremio.agregar_mision(mision):
                print("\n Misión registrada exitosamente!\n")
            else:
                print("\n Ya existe una misión con el mismo nombre.\n")

    def realizar_mision(self):
        print("Realizar misión")

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



    def ver_top_aventureros_mas_misiones_resueltas(self):
        print("\nTop 10 de aventureros con más misiones resueltas\n")
        top = self.gremio.top_10_aventureros_misiones()
        for indice, nombre in top:
            print(f"{indice}. {nombre}")


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
                while True:
                    self.display_submenu_consultas()
                    opcion_submenu = self.get_valid_input("Ingrese la opción deseada: ", ["1", "2", "3", "4"])
                    if opcion_submenu == "1":
                        pass 
                    elif opcion_submenu == "2":
                        pass
                    elif opcion_submenu == "3":
                        pass
                    elif opcion_submenu == "4":
                        break
            elif opcion == "5":
                break