

from clases import *
from clases.utils import *

if __name__ == '__main__':
    
    with open("configs/config.json", "r") as file:
        config = json.load(file)

    game = GameManager(config)

    game.run()





"""

Prototipo del gameloop:

    Init: load configs, initialize gameloop variables

    While True:

        While True:
            Run menu
    
        while game.exit() not False:
            Run scene Manager

        if exit
            brake    

"""