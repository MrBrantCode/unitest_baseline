"""
QUESTION:
Create a function named `gradient_descent` that uses gradient descent to find the global minimum of the function y = x^2. The function should take three parameters: the initial value `x_start`, the learning rate `learn_rate`, and the number of iterations `n_iter`. The function should return a numpy array of the history of x values throughout the iterations.
"""

import numpy as np

def gradient_descent(x_start, learn_rate, n_iter):
    x = x_start
    history = np.zeros(n_iter+1)
    history[0] = x
    
    for i in range(n_iter):
        grad = 2*x  # Gradient of our function 
        x = x - learn_rate*grad
        history[i+1] = x
        
    return history