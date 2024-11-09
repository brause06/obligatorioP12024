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
            

