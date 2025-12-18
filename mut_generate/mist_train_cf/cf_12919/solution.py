"""
QUESTION:
Implement a function `sqrt_newton_raphson(N, epsilon=1e-6)` that calculates the square root of a given number `N` using the Newton-Raphson method. The function should take two parameters: `N` (the number to find the square root of) and `epsilon` (the desired level of accuracy, defaulting to 1e-6). The function should return the square root of `N`.
"""

def sqrt_newton_raphson(N, epsilon=1e-6):
    x = N / 2  # Initial approximation

    while True:
        fx = x**2 - N  # f(x_n)
        fpx = 2 * x  # f'(x_n)

        x_next = x - fx / fpx  # Calculate next approximation

        if abs(x_next - x) < epsilon:  # Check convergence
            break

        x = x_next  # Update approximation

    return x_next