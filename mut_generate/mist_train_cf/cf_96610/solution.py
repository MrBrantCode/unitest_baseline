"""
QUESTION:
Evaluate a polynomial equation for a given list of values. 

Write a function named `evaluate_polynomial` that takes two lists of numbers: `coefficients` and `values`. The `coefficients` list represents the coefficients of a polynomial equation in ascending order of degree, starting with the coefficient for the highest degree term. The `values` list represents the values to be substituted into the equation. The function should return a new list that contains the results of evaluating the polynomial equation for each value in the `values` list. The polynomial equation can be of any degree up to and including degree 10.
"""

def evaluate_polynomial(coefficients, values):
    results = []
    degree = len(coefficients) - 1
    
    for value in values:
        result = 0
        
        for i in range(degree + 1):
            result += coefficients[i] * (value ** (degree - i))
        
        results.append(result)
    
    return results