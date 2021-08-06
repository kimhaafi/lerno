import numpy as np

def Relu(x):
    zero_array = np.zeros(x.shape, dtype=x.dtype)
    result = np.maximum(x, zero_array)
    
    return result