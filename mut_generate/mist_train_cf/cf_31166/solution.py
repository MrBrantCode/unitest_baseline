"""
QUESTION:
Implement the `lorentzian(x, amplitude, x0, sigma, background)` function, which calculates the value of a Lorentzian peak function. The function should take five parameters: `x`, `amplitude`, `x0`, `sigma`, and `background`, and return the value of the Lorentzian peak function at `x` using the formula `f(x) = amplitude / (1 + ((x - x0) / sigma) ** 2) + background`.
"""

def lorentzian(x, amplitude, x0, sigma, background):
    return amplitude / (1 + ((x - x0) / sigma) ** 2) + background