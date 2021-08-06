import numpy as np

class Relu:
    def activate(x):
        zero_array = np.zeros(x.shape, dtype=x.dtype)
        result = np.maximum(x, zero_array)

        return result

    def derivative(x):
        return 1 if x > 0 else 0
