import random
from typing import Tuple, Sequence
import numpy as np

class agent:
    def __init__(self, *, dims: Tuple[int, ...]):
        assert len(dims) >= 2, 'Error: dims must be two or higher.'
        self.dims = dims
        self._DNA = []
        self.score = 0
        self.id = 0
        self.mutation_rate = 1
        for i, dim in enumerate(dims):
            if i < len(dims) - 1:
                self._DNA.append(np.random.rand(dim, dims[i + 1]))

        # Convert DNA to a tuple to ensure it's immutable
        self._DNA = tuple(map(np.copy, self._DNA))

    @property
    def DNA(self):
        # Return a copy to ensure immutability
        return tuple(map(np.copy, self._DNA))
    
    def set_dna(self,data):
        self._DNA = data
        
    def update(self, obs: Sequence) -> Tuple[int, int, int, int]:
        x = obs
        for i, layer in enumerate(self._DNA):
            if not i == 0:
                x = leaky_relu(x)
            x = x @ layer
        return softmax(x)

    def action(self, obs: Sequence):
        return self.update(obs).argmax()

    def mutate(self):
        # Create a new instance of the agent with mutated DNA
        mutated_DNA = list(map(np.copy, self._DNA))
        random_layer = random.randint(0, len(mutated_DNA) - 1)
        row = random.randint(0, mutated_DNA[random_layer].shape[0] - 1)
        col = random.randint(0, mutated_DNA[random_layer].shape[1] - 1)
        mutated_DNA[random_layer][row][col] = random.uniform(-1, 1)
        mutated_agent = type(self)(dims=self.dims)
        mutated_agent._DNA = tuple(mutated_DNA)
        mutated_agent.score = self.score
        return mutated_agent

    def __add__(self, other):
        baby_DNA = []
        for mom, dad in zip(self._DNA, other._DNA):
            if random.random() > 0.5:
                baby_DNA.append(mom)
            else:
                baby_DNA.append(dad)
        baby = type(self)(dims=self.dims)
        # Convert baby_DNA to a tuple to ensure it's immutable
        baby._DNA = tuple(map(np.copy, baby_DNA))
        return baby

    def __str__(self):
        return f'agent points({self.score})'

def softmax(z):
    return np.exp(z) / np.sum(np.exp(z))

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def tanh(z):
    return np.tanh(z)

def relu(z):
    return np.maximum(0, z)

def leaky_relu(z):
    epsilon = 0.001
    return np.maximum(z * epsilon, z)
