from ga_model import agent
from controller import controller
import numpy as np
from cargame import CarGame
import asyncio

class GA_controller(controller):

    def __init__(self,game: CarGame) -> None:
        self.population:list[agent] = []
        self.draw = False
        self.game = game
        self.game.controller = self
        self.population_number = 52
        self.intialize_population(self.population_number)
        self.current_runner = 0
             
    def intialize_population(self,count:int):
        self.population = [agent(dims=[4,4,4]) for _ in range(count)]   
        
    def update(self, data) -> tuple[int,int,int,int]:
        test = self.population[self.current_runner].update(data)
        updated = np.where(test>0.5, 1,0)
        
        return updated
    def run(self):
        for i in range(10):
            print(f"Evolution number: {i}")
            self.evolve()
        sorted_population = sorted(self.population, key=lambda x: x.score)
        print(sorted_population[-1].DNA)
        input("watch run")

        self.draw = True
        self.game.__init__()
        self.game.run()


        

    def evolve(self):
        self.run_generation()
        #select best
        sorted_population = sorted(self.population, key=lambda x: x.score)
        self.population = sorted_population[int(self.population_number/2):]
        #procreate
        for i in range(0,int(self.population_number/2),2):
            mom = self.population[i]
            dad = self.population[i+1]
            self.population.append(mom + dad)
            self.population.append(mom + dad)
        #try agaain
        for i in self.population:
            i.mutate()
    def run_generation(self):
        for _ in self.population:
            self.game.__init__()

            points = self.game.run()
            self.population[self.current_runner].score = points
            self.game.running = False
            self.current_runner +=1
            
        self.current_runner = 0
        print(max(self.population, key=lambda x: x.score))
