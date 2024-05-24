from ga_model import agent
from controller import controller
import numpy as np
class GA_controller(controller):

    def __init__(self) -> None:
        self.population:list[agent] = []
        self.draw = False
        self.intialize_population(2)
             
    def intialize_population(self,count:int):
        self.population = [agent(dims=[4,4,4,4]) for _ in range(count)]   
        
    def update(self, data) -> tuple[int,int,int,int]:
        test = self.population[0].update(data)
        updated = np.where(test>0.4, 1,0)
        
        return updated
