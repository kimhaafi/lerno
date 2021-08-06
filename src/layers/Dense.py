import numpy as np 
from . import Neuron

class Dense():
    def __init__(self, size, output_size, activation, parent=None):
        self.neurons = [Neuron(output_size)] * size
        self.bias = 0
        self.output_size = output_size
        self.activation = activation
        self.parent = parent

    def forward(self, input):
        result = np.zeros(self.output_size)
        for neuron in self.neurons:
            result += self.activation.activate(np.dot(input, neuron.weights) + self.bias)

        return result

    def backward(self, output, expected):	
        error = (expected - output) * self.activation.derivative(output)
