from cargame import CarGame 
from human_controller import human_controller as hu
from ga_controller import GA_controller as ga
from seeded_controller import seeded_controller as su

if __name__ == '__main__':
    decider = 3
    game = CarGame()

    if(decider == 1):
        controller = hu(game)
    elif(decider == 2):
        controller = su(game)
        controller.load_DNA(DNA=[([[0.99665831, 0.05243759, 0.53031074, 0.05532557],
       [0.0315358 , 0.75826636, 0.06175348, 0.82007059],
       [0.67107397, 0.0795316 , 0.17378135, 0.97396575],
       [0.88875863, 0.06276549, 0.01593386, 0.60415906]]), ([[5.61739863e-04, 1.79159776e-01, 3.14630371e-01, 4.36955800e-01],
       [7.50482925e-01, 9.74500286e-01, 5.25098799e-02, 3.92242481e-01],
       [8.60850761e-01, 5.31417843e-01, 5.33039989e-01, 1.50138694e-02],
       [1.17219471e-01, 1.55007202e-01, 2.13146369e-01, 7.16854824e-01]])])
    else:        
        controller = ga(game)
        
    controller.run()
