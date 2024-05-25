from ga_model import agent
from controller import controller
import numpy as np
from cargame import CarGame
import asyncio
import time
import asyncio

class GA_controller(controller):

    def __init__(self,game: CarGame) -> None:
        self.population:list[agent] = []
        self.draw = False
        self.game = game
        self.game.controller = self
        self.population_number = 500
        self.intialize_population(self.population_number)
        self.current_runner = 0
             
    def intialize_population(self,count:int):
        self.population = [agent(dims=[4,4,8,4]) for _ in range(count)]   
        
    def update(self, data,index) -> tuple[int,int,int,int]:
        test = self.population[index].update(obs=data)
        updated = np.where(test>0.5, 1,0)
        
        return updated
    def run(self,times=1):
        command = "c"
        itteration = 1
        while command != "q":
            self.current_runner = 0
            if(command == "c"):
                for _ in range(times):
                    start = time.time()

                    print(f"Evolution number: {itteration} start")
                    self.evolve()
                    end = time.time()
                    print(f"Evolution number: {itteration} end, took {end-start}")
                    itteration += 1
                print("------------------------------------------")
                sorted_population = sorted(self.population, key=lambda x: x.score)
                print(sorted_population[-1].index)
                print(sorted_population[-1].score)

            print("type 'c' to continue evolving")
            print("type 'w' to watch the best run of the previous generation")
            print("type 'q' to quit")
            command = input("").lower()
            if(command == "w"):
                self.current_runner= self.population.index(max(self.population, key=lambda x: x.score))
                self.draw = True
                self.game.__init__()
                self.game.run(index=self.current_runner)
                self.draw = False
                self.game.__del__()



        

    def evolve(self):
        self.run_generation()
        #select best
        sorted_population = sorted(self.population, key=lambda x: x.score)
        print(f"before: {[x.score for x in sorted_population]}")
        temp = sorted_population[int(self.population_number/2):]
        self.population = temp
        print(f"selected sample:{[x.score for x in temp]}")
        #procreate
        for i in range(0,int(self.population_number/2),2):
            mom = self.population[i]
            dad = self.population[i+1]
            self.population.append(mom + dad)
            self.population.append(mom + dad)
        #try agaain
        for i in self.population:
            i.mutate()
        sorted_population = sorted(self.population, key=lambda x: x.score)
    def run_generation(self):
        for i in range(len(self.population)):
            self.run_game(i)

        print(max(self.population, key=lambda x: x.score))

    def run_game(self, i: int) -> int:
        game = CarGame()
        game.controller = self
        game.__init__()
        points = game.run(i)
        self.population[i].score = points
        game.__del__()
        return points