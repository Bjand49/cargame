from cargame import CarGame 
from human_controller import human_controller as hu
from ga_controller import GA_controller as ga
if __name__ == '__main__':
    game = CarGame(ga())
    game.run()
