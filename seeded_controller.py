from ga_model import agent
from controller import controller
import numpy as np
from cargame import CarGame
class seeded_controller(controller):

    def __init__(self,game: CarGame) -> None:
        self.population:list[agent] = []
        self.draw = True
        self.game = game
        self.game.controller = self
        self.agent = None
        self.game.controller = self


    def load_DNA(self,DNA):
        self.agent = agent(dims=[4,4,4])
        self.agent.DNA = DNA
        
    def update(self, data) -> tuple[int,int,int,int]:
        test = self.agent.update(data)
        updated = np.where(test>0.5, 1,0)
        
        return updated
    def run(self):
        self.game.run()

