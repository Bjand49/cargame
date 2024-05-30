from cargame import CarGame 
from human_controller import human_controller as hu
from ga_controller import GA_controller as ga
from seeded_controller import seeded_controller as su
from pickle4 import pickle

if __name__ == '__main__':
    controller = None
    map = 'road'
    data = ""
    while True:
        print("type '1' to play as a human")
        print("type '2' to watch the best run of the previous generation")
        print("type '3' to work the AI")
        print("type 'q' to quit the game")
            

        decider = input("").lower()
        print(map)
        if(decider == "1"):
            controller = hu(CarGame(map=map))
        elif(decider == "2"):
            print("input filename")
            dna_file = input("").lower()
            try:
                data = pickle.load(open(dna_file+'.txt', 'rb'))
            except:
                if(data is ""):
                    print("please input real data")
                print("invalid file, using previous")
            controller = su(CarGame(map=map))
            controller.load_DNA(DNA=data)
        elif (decider == "3"):        
            controller = ga(CarGame(map=map))
        elif(decider == "q"):
            break
        elif(decider == "r"):
            print("write mapname:")
            map = input("").lower()
        if(controller is not None):
            controller.run()
        controller = None
