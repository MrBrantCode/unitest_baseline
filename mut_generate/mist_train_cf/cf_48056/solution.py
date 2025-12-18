"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a given non-negative integer `n`. The function should handle large values of `n` efficiently and include error handling for invalid inputs, such as negative numbers and non-integer values. If an invalid input is provided, the function should return a meaningful error message.
"""

def factorial(n, memo = {}):
    # check if n is not integer
    if not isinstance(n, int):
        return "Error: Invalid Input! Please enter a non-negative integer."
    
    # check if n is a negative integer
    elif n < 0:
        return "Error: Invalid Input! Please enter a non-negative integer."
            
    if n == 0 or n == 1:
        return 1
    
    # check if we have already calculated factorial(n)
    elif n in memo:
        return memo[n]
    
    memo[n] = n * factorial(n-1)
    
    return memo[n]