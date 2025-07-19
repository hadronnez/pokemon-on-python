
from clases.Pokemon import Pokemon
from clases.Combate import Combate

if __name__ == '__main__':
    pikachu = Pokemon("Pikachu", 20, 10, 10, 10)
    charmander = Pokemon("Charmander", 20, 15, 5, 10)

    Combate(pikachu, charmander, 100)

    print(pikachu.estado())
    print(charmander.estado())

    pikachu.curar()
    charmander.curar()

    print(pikachu.estado())
    print(charmander.estado())

    Combate(pikachu.subida_nivel().subida_nivel().curar(), charmander, 100)
    Combate(pikachu, charmander.curar(), 100)