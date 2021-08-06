import numpy as np

def Rectifier(z):
    return np.log(1 + np.exp(z))