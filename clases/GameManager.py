
from .SceneManager import SceneManager
from clases.utils import *


class GameManager:

    def __init__(self, config: dict) -> None:
        self.running = True
        self.option = "0"
        self.filesave = " "
        self.config = config
        self.scene_manager = SceneManager()


    def run(self) -> None:

        while self.running:

            self.run_menu()
            self.load_filesave()

            if self.running:
                while True:
                    print("Hemos entrado en el bucle de escenas")
                    self.scene_manager.handle_input()
                    self.scene_manager.update()
                    self.scene_manager.render()

            if self.scene_manager.should_quit():
                self.running = False

        self.run_ending()


    def run_menu(self) -> None:

        print("\n----BIENVENIDO A POKEMON-ON-PYTHON----\n")
        while self.option not in ("1","2","3"): 
            self.option = input("\n¿Deseas empezar una nueva aventura (1), continuarla (2) o salir del juego (3)? ")
            if self.option not in ("1","2","3"):
                print("Esa opción no es válida.")


    def load_filesave(self) -> None:

        if self.option == "1":
            with open("saves/default_filesave.json", "r") as file:
                self.filesave = json.load(file)
        elif self.option == "2":
            with open("saves/ongoing_filesave.json", "r") as file:
                self.filesave = json.load(file)
        elif self.option == "3":
            self.quit()
        else:
            print("Ha habido un problema")
            

    def quit(self):
        self.running = False


    def run_ending(self):
        print("El juego ha finalizado.")
        