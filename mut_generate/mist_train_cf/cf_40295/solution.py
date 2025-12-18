"""
QUESTION:
Implement a function `calculatePsi(n, X, E)` that calculates the value of Psi[n] for a given positive integer n, X, and E, based on the equation Psi[n] = F(X, E) * Psi[n-1] and the initial condition Psi[1] = 1. 

- The function takes in three parameters: `n` (1 <= n <= 100), a positive integer, and `X` and `E`, floats used in the function F.
- The function should return the value of Psi[n].
"""

def calculatePsi(n, X, E):
    def f(x, e):
        # Function F(X, E) implementation should be provided to use this function
        pass
    
    if n == 1:
        return 1
    else:
        return f(X, E) * calculatePsi(n-1, X, E)