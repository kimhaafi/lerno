import numpy as np 

class Dense():
    def __init__(self, activation):
        self.units = []
        self.bias = 0
        self.activation = activation

    def forward(self, input):
        return self.activation(np.dot(input, self.units) + self.bias)