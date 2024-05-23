from ga_model import ga_model
from controller import controller

class GA_controller(controller):
    def __init__(self) -> None:
        self.population:list[ga_model] = []
        
        
    def intialize_population(self,count:int = 200):
        self.population = [self.create_agent() for _ in range(count)]

    def create_agent(self): 
        agent = ga_model()
        agent.DNA = self.random_DNA(); 
    
    def random_DNA(self):
        for i in range(self.layer_count):
            pass
        
    def update(self, data):
        pass

class ga_model:
    def __init__(self) -> None:
        self.mutationrate = 0.2
        self.layer_count = 2
