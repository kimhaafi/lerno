import numpy as np
import math

def Rectifier(z):
    return np.log(1 + math.exp(z))