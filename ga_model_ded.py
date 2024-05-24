import numpy as np
import random
import tensorflow as tf

class agent:
    global num_input_nodes
    global num_output_nodes
    def __init__(self, dna=None):
        self.num_input_nodes,self.create_neural_networknum_output_nodes = 4
        
        if dna is None:
            self.dna = self.generate_dna()
        else:
            self.dna = dna
        self.decode_dna()
        
    @staticmethod
    def create_random_agent(num_input_nodes:int = 4,num_output_nodes:int = 4):
        num_hidden_layers = random.randint(1, 3)
        hidden_layer_sizes = [random.randint(5, 20) for _ in range(num_hidden_layers)]
        layer_sizes = [num_input_nodes] + hidden_layer_sizes + [num_output_nodes]
        activation_functions = [random.randint(1, 2) for _ in range(len(layer_sizes) - 1)]  # 1 for ReLU, 2 for sigmoid, evt 3,4,5 for other functions

        learning_rate = random.uniform(0.0001, 0.01)
        beta1 = random.uniform(0.8, 0.999)
        beta2 = random.uniform(0.9, 0.9999)
        epsilon = random.uniform(1e-8, 1e-6)

        weights_and_biases = []
        for i in range(len(layer_sizes) - 1):
            weights = np.random.randn(layer_sizes[i], layer_sizes[i + 1]).flatten().tolist()
            biases = np.random.randn(layer_sizes[i + 1]).flatten().tolist()
            weights_and_biases.extend(weights + biases)

        dna = [num_hidden_layers] + hidden_layer_sizes + activation_functions + [learning_rate, beta1, beta2, epsilon] + weights_and_biases
        return dna

    def decode_dna(self):
        # Decode the DNA
        self.layers = self.dna[0]
        self.neurons = self.dna[1:5]
        self.activations = self.dna[5:9]
        self.learning_rate = self.dna[9]
        self.beta1 = self.dna[10]
        self.beta2 = self.dna[11]
        self.epsilon = self.dna[12]
        self.weights_and_biases = self.dna[13:]
    
    def set_fitness(self,score:int):
        self.fitness = score
        
    @staticmethod
    def crossover(parent1, parent2):
        # Create a new DNA by combining the parents' DNAs
        child_dna = []
        for gene1, gene2 in zip(parent1.dna, parent2.dna):
            child_dna.append(gene1 if np.random.rand() < 0.5 else gene2)
        return agent(dna=child_dna)

    def mutate(self, mutation_rate=0.01):
        
        # Mutate the DNA by randomly changing some genes
        for i in range(len(self.dna)):
            if np.random.rand() < mutation_rate:
                self.dna[i] += np.random.normal(0, 0.1)
                
    def create_neural_network(self,dna):
        params = self.decode_dna(dna)
        model = tf.keras.Sequential()
        
        # Input layer
        model.add(tf.keras.layers.InputLayer(input_shape=(num_input_nodes,)))

        # Hidden layers
        for i in range(1, len(params['layer_sizes']) - 1):
            model.add(tf.keras.layers.Dense(params['layer_sizes'][i], activation=get_activation_function(params['activation_functions'][i - 1])))
        
        # Output layer
        model.add(tf.keras.layers.Dense(params['layer_sizes'][-1], activation=get_activation_function(params['activation_functions'][-1])))

        # Set weights and biases
        for i, layer in enumerate(model.layers):
            weights, biases = params['weights'][i], params['biases'][i]
            layer.set_weights([weights, biases])

        # Compile model with Adam optimizer
        optimizer = tf.keras.optimizers.Adam(
            learning_rate=params['learning_rate'],
            beta_1=params['beta1'],
            beta_2=params['beta2'],
            epsilon=params['epsilon']
        )
        model.compile(optimizer=optimizer, loss='mse')

        return model
