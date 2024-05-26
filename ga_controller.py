from ga_model import agent
from controller import controller
import numpy as np
from cargame import CarGame
import time
from pickle4 import pickle
class GA_controller(controller):

    def __init__(self,game: CarGame) -> None:
        self.population:list[agent] = []
        self.draw = False
        self.game = game
        self.game.controller = self
        self.population_number = 20 * 2 * 2
        self.generations=[]
        self.itteration = 0
        self.current_agent = None
        self.intialize_population(self.population_number)
        
    def intialize_population(self,count:int):
        self.population = [agent(dims=[4,4,4]) for _ in range(count)]
        
    def update(self, data, id) -> tuple[int,int,int,int]:
        test = self.current_agent.update(obs=data)
        updated = np.where(test>0.4, 1,0)
        
        return updated
    def run(self,times=20):
        command = "c"
        self.itteration = 0
        while command != "q":
            if(command == "c"):
                for _ in range(times):
                    start = time.time()
                    print(f"Evolution number: {self.itteration} start")

                    self.evolve()
                    print()

                    end = time.time()
                    scores = [x.score for x in self.population]
                    print(max(scores))
                    print(f"Average Score: {sum(scores)/len(self.population)}")
                    print(f"Evolution number: {self.itteration} end, took {end-start}")
                    print("------------------------------------------")
                
                    self.itteration += 1
                print("##########################################################################")
                sorted_population = sorted(self.population, key=lambda x: x.score)
                print(sorted_population[-1].score)

            print("type 'c' to continue evolving")
            print("type 'w' to watch the best run of the previous generation")
            print("type 'q' to quit")
            print("type 'asdf' to test")
            
            command = input("").lower()
            if(command == "w"):
                self.draw = True
                self.game.__init__()
                self.current_agent = sorted_population[-1]
                self.game.run(id=sorted_population[-1].id)
                self.draw = False
                self.game.__del__()
            if(command == "asdf"):
                print(self.generations)
            if(command == "p"):
                with open("saved_agent.txt", "wb") as file:
                    file.write(pickle.dumps(sorted_population[-1].DNA))

    def evolve(self):
        #select best
        if(self.current_agent is not None):
            self.generations.append({'generation':self.itteration, 'data':[x.score for x in self.population]})
        self.population.sort(key=lambda x: x.score, reverse=True)
        print(f"Points: {[x.score for x in self.population]}")
        
        num_selected = len(self.population) // 2
        selected_agents = self.population[:num_selected]
        
        self.population.clear()

        i = 0

        while len(selected_agents) != self.population_number:
            mom, dad = selected_agents[i], selected_agents[i+1] 
            child1, child2 = mom + dad, mom + dad
            
            child1= child1.mutate()
            child2= child2.mutate()
            selected_agents.append(child1)
            selected_agents.append(child2)
            i+= 2
        self.population = selected_agents
        for id,agent in enumerate(self.population):
            agent.id = id
        self.population.sort(key=lambda x: x.score, reverse=True)

        self.run_generation()

            
    def run_generation(self):
        for agent in self.population:
            score1 = agent.score
            self.run_game(agent)
            score2 = agent.score
        print(max(self.population, key=lambda x: x.score))

    def run_game(self, agent) -> int:
        self.game.__init__()
        self.current_agent = agent
        points = self.game.run(agent.id)
        agent.score = points
        self.game.__del__()
        return points
