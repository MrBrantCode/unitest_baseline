"""
QUESTION:
Create a function named `weighted_sum` that takes two variables `x` and `y`, and an array of two coefficients. The function should calculate the square of `x` and `y`, then return the weighted sum of these squared values using the provided coefficients. The function must handle potential exceptions if the coefficients array does not have exactly 2 elements or if any of the coefficients are not numeric.
"""

def weighted_sum(x, y, coefficients):
    #Check if coefficients list is of length 2
    if len(coefficients) != 2:
        return "Error: Coefficients array must have 2 elements."
  
    #Check if coefficients list elements are numbers
    for coeff in coefficients:
        if not isinstance(coeff, (int, float)):
            return "Error: All coefficients must be numeric."
    
    #Square the variables
    x2, y2 = x**2, y**2
  
    #Calculate and return the weighted sum
    return coefficients[0]*x2 + coefficients[1]*y2