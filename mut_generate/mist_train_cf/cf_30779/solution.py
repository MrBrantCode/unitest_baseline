"""
QUESTION:
Implement the function `gradient_descent_for_function` that performs gradient descent on a given function `f` with one variable. The function should take as input the function `f`, the initial guess `x0`, the step size, and optional parameters `max_iterations` and `epsilon`. The function should return a dictionary containing the final value of `x`, the minimum value of the function, and the history of function values and `x` values during the iterations. The function should iterate until `max_iterations` is reached or the change in `x` is less than `epsilon`.
"""

import numpy as np

def gradient_descent_for_function(f, x0, step_size, max_iterations=1000, epsilon=1e-6):
    x = x0
    f_history = []
    x_history = []

    for _ in range(max_iterations):
        gradient = (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)
        x = x - step_size * gradient
        f_history.append(f(x))
        x_history.append(x)

        if abs(gradient) < epsilon:
            break

    return {"x": x, "f": f(x), "f_history": f_history, "x_history": x_history}