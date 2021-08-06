import numpy as np

class Neuron:
    def __init__(self, output_size):
        self.weights = np.random.rand(output_size)
        self.delta = 0