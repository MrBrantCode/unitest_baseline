"""
QUESTION:
Implement a function named `gradient_descent` that takes three parameters: `start_x`, `learning_rate`, and `iteration`. The function should use the gradient descent algorithm to find the minimum of a given function `f(x) = (x - 5)²` with its derivative `f'(x) = 2 * (x - 5)`. The function should iterate `iteration` times, update the value of `x` based on the current gradient and `learning_rate`, and return the final value of `x`.
"""

def gradient_descent(start_x, learning_rate, iteration):
    x = start_x
    for i in range(iteration):
        grad = 2 * (x - 5)
        x = x - learning_rate * grad
    return x