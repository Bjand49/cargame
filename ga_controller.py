from ga_model import agent
from controller import controller
from cargame import CarGame
import numpy as np
class GA_controller(controller):

    def __init__(self) -> None:
        self.population:list[agent] = []
        self.num_input_nodes = 4
        self.num_output_nodes = 4
        self.draw = False
        self.intialize_population(1)
             
    def intialize_population(self,count:int):
        self.population = [agent(dims=[4,4,4]) for _ in range(count)]   
        
    def update(self, data) -> tuple[int,int,int,int]:
        test = self.population[0].update(data)
        updated = np.where(test>0.2, 1,0)
        
        return updated
