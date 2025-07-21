
from .SceneManager import SceneManager

class GameManager:

    def __init__(self, config: dict) -> None:
        self.running = True
        self.config = config
        self.scene_manager = SceneManager()


    def run(self):

        while self.running:

            self.initialize()
            if False:
                self.scene_manager.handle_input()
                self.scene_manager.update()
                self.scene_manager.render()

            if self.scene_manager.should_quit():
                self.running = False

        self.finalize()

    def initialize(self) -> None:

        print("\n----BIENVENIDO A POKEMON-ON-PYTHON----\n")
        
        menu = "0"

        while menu not in ("1","2","3"): 
            menu = input("¿Deseas empezar una nueva aventura (1), continuarla (2) o salir del juego (3)? ")
            if menu in ("1","2","3"):
                break

        if menu == "1":
            pass
        elif menu == "2":
            pass
        elif menu == "3":
            self.quit()
        else:
            print("Ha ocurrido un error.")



    def load_state(self) -> str:
        return input("Selecciona el archivo de guardado que quieres cargar (1,2 o 3): ")
        
    def quit(self):
        self.running = False
    
    def finalize(self):
        print("El juego ha finalizado.")
        