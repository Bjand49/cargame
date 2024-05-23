from cargame import CarGame 
from human_controller import human_controller
if __name__ == '__main__':
    game = CarGame()
    game.controller = human_controller(game)
    game.run()
