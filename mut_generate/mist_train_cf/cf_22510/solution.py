"""
QUESTION:
Create a function named `binomial_coefficients(n)` that calculates and returns the binomial coefficients for a given positive integer `n`. The function should handle large numbers efficiently with a time complexity of O(n) or better and should check if the input is a positive integer. If the input is not a positive integer, the function should return an error message.
"""

def binomial_coefficients(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer."
    
    coefficients = [[1]]
    
    for i in range(1, n + 1):
        row = [1]
        for j in range(1, i):
            row.append(coefficients[i - 1][j - 1] + coefficients[i - 1][j])
        row.append(1)
        coefficients.append(row)
    
    return coefficients