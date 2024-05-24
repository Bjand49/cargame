from cargame import CarGame 
from human_controller import human_controller as hu
from ga_controller import GA_controller as ga
if __name__ == '__main__':
    decider = 1
    if(decider == 1):
        controller = hu()
        game = CarGame(controller)
        controller.game = game
    else:        
        controller = ga()
        game = CarGame(controller)
    game.run()
