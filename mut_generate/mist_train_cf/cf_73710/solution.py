"""
QUESTION:
Given a discriminative model with parameters 'w', define the function `discriminative_model` that models the conditional probability of the output 'y' given the input 'x'. The function should not take any arguments other than 'x' and 'w'.
"""

def discriminative_model(x, w):
    import numpy as np
    return 1 / (1 + np.exp(-np.dot(x, w)))