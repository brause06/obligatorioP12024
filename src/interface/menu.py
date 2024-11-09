from obligatorioP12024.src.models.gremio import Gremio


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
        pass

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