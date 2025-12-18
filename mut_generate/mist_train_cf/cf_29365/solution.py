"""
QUESTION:
Implement a function `optimize_function` that takes a function `fun`, an initial guess `x0`, a learning rate `alpha`, an array of deltas `deltas`, and an index `where` as input. The function should use the Nelder-Mead method to optimize the given function `fun` and return the optimized score and the updated `x`. The optimization process should involve updating the variable `x` using the calculated direction and the learning rate `alpha`, setting any negative values in `x` to 0 after the update, and calculating the score using the updated `x`.
"""

import numpy as np

def optimize_function(fun, x0, alpha, deltas, where):
    x = x0  
    direction = deltas[where]
    direction /= np.mean(np.abs(direction))

    x -= alpha * direction * x  
    x[x < 0] = 0  

    score = fun(x)  

    return score, x