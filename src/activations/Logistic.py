import numpy as np

def Logistic(z):
    return 1 / (1 + np.exp(-z))