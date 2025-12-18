"""
QUESTION:
Implement a function `proximal_gradient_descent` that takes the following inputs:
- `x`: ndarray - the current estimate of the solution
- `gradfx`: ndarray - the gradient of the objective function at `x`
- `prox`: function - the proximal operator that enforces additional constraints
- `f`: function - the objective function to be minimized
- `linesearch`: bool - a flag indicating whether to perform line search

The function should return the updated estimate `x` after performing proximal gradient descent using the Armijo-Goldstein condition for line search to determine the optimal step size `tau`. The Armijo-Goldstein condition should be implemented using the inequality `f(x - tau * gradfx) <= f(x) - alpha * tau * np.dot(gradfx, gradfx)`, where `alpha` is a constant in the range (0, 0.5) that controls the step size. If `linesearch` is False, the function should return the updated estimate `x` without performing line search.
"""

import numpy as np

def proximal_gradient_descent(x, gradfx, prox, f, linesearch=True, alpha=0.3, beta=0.5):
    tau = 1.0  
    while True:
        x_hat = x - tau * gradfx
        z = prox(x_hat, tau)
        fz = f(z)
        if not linesearch:
            x = z
            break
        if fz <= f(x) - alpha * tau * np.dot(gradfx, gradfx):
            x = z
            break
        else:
            tau *= beta  
    return x