
from clases import *

if __name__ == '__main__':
    
    pikachu = Pokemon("Pikachu", 20, 10, 10, 10)
    charmander = Pokemon("Charmander", 20, 15, 5, 10)

    Combate(pikachu.subida_nivel().subida_nivel().curar(), charmander, 100)