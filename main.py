from cargame import CarGame 
from human_controller import human_controller as hu
from ga_controller import GA_controller as ga
from seeded_controller import seeded_controller as su
from pickle4 import pickle

if __name__ == '__main__':
    controller = None
    game = CarGame()

    while True:
        print("type '1' to play as a human")
        print("type '2' to watch the best run of the previous generation")
        print("type '3' to work the AI")
        print("type 'q' to quit the game")
            

        decider = input("").lower()

        if(decider == "1"):
            controller = hu(game)
        elif(decider == "2"):
            data = pickle.load(open('saved_agent.txt', 'rb'))
            controller = su(game)
            controller.load_DNA(DNA=data)
        elif (decider == "3"):        
            controller = ga(game)
        elif(decider == "q"):
            break
        if(controller is not None):
            controller.run()
