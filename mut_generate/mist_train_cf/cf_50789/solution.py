"""
QUESTION:
Implement a gradient descent algorithm with the function name `gradient_descent` that takes the cost function `func`, its derivative `derivative`, initial point `initial_point`, learning rate `learning_rate`, maximum number of iterations `max_iters`, and precision `precision` as parameters. The algorithm should iteratively update the current point to minimize the cost function and stop when the parameters stop changing significantly or the maximum number of iterations is reached. Assume that the cost function is convex.
"""

import numpy as np

def gradient_descent(func, derivative, initial_point, learning_rate=0.1, max_iters=10000, precision=0.0001):
    current_point = initial_point
    step_sizes = [1]
    
    iter_counter = 0
    while np.sum(np.square(step_sizes)) > precision**2 and iter_counter < max_iters:
        prev_point = current_point
        current_point = prev_point - learning_rate * derivative(prev_point)
        
        # Calculate the change in the parameters to assess convergence
        step_sizes = current_point - prev_point
        
        iter_counter += 1
    
    return current_point