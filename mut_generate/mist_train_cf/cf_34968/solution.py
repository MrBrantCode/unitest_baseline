"""
QUESTION:
Implement a function `calculate_derivative(i_calc, eps)` to calculate the derivative of a given mathematical function `f` using the finite difference method. The function `calculate_derivative` should iterate through the values in `i_calc`, apply the finite difference method to estimate the derivative at each point, and return a list of derivative values. Assume the mathematical function `f` is defined elsewhere and can be called with a single argument. The `eps` parameter represents the small change in the input used for the finite difference method. The `i_calc` object has a `size()` method that returns the number of values to iterate through.
"""

def calculate_derivative(i_calc, eps, f):
    derivatives = []
    for ih in range(i_calc.size()):
        c_orig = i_calc[ih]
        f_plus = f(c_orig + eps)
        f_minus = f(c_orig - eps)
        derivative = (f_plus - f_minus) / (2 * eps)
        derivatives.append(derivative)
    return derivatives