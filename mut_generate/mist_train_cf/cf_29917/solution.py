"""
QUESTION:
Implement a function named `gradient_descent` that takes four inputs: the initial guess `x0`, the learning rate, the maximum number of iterations, and the objective function to be minimized. The function should perform gradient descent optimization to find the minimum of the objective function and return the estimated minimum value, the number of iterations performed, and the sequence of intermediate values obtained during the optimization process.
"""

def entrance(x0, learning_rate, max_iterations, objective_function):
    xks = [x0]
    it = 0
    while it < max_iterations:
        xk = xks[-1]
        gradient = (objective_function(xk + 0.0001) - objective_function(xk)) / 0.0001  # Approximate gradient
        xk -= learning_rate * gradient
        xks.append(xk)
        it += 1
    if it == max_iterations:
        print("Maximum number of iterations reached")
    return xks[-1], it, xks